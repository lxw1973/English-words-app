from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import get_db, engine
from app.models import Base, DifficultyLevel, Word
from app.schemas import WordResponse, WordCreate, LearningRecordUpdate
from app.services.word_service import WordService
from app.services.ai_service import WordGenerator
import asyncio

# 创建表
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="英语单词学习系统",
    description="AI驱动的英语单词学习应用",
    version="1.0.0"
)

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

word_generator = WordGenerator()


# ==================== 词库管理 ====================

@app.post("/api/words/generate")
async def generate_words(
        difficulty: DifficultyLevel,
        count: int = Query(10, ge=1, le=100),
        db: Session = Depends(get_db)
):
    """AI生成词库（累计去重：已存在的单词跳过，不计入新增数）"""
    generated_words = []
    added_count = 0

    for _ in range(count):
        try:
            word_data = await word_generator.generate_word(difficulty, db)
            exists = db.query(Word).filter(Word.word == word_data.get("word")).first()
            if exists:
                continue  # 已存在，跳过（去重累计）
            word_obj = WordService.create_word(db, WordCreate(**word_data))
            generated_words.append(word_obj)
            added_count += 1
        except Exception as e:
            print(f"生成失败: {e}")
            continue

    return {
        "status": "success",
        "message": f"成功新增{added_count}个单词（已跳过{count - added_count}个重复）",
        "words": [WordService.to_response_with_proficiency(db, w) for w in generated_words]
    }


@app.get("/api/words")
def get_words(
        difficulty: DifficultyLevel = Query(DifficultyLevel.CET4),
        skip: int = Query(0),
        limit: int = Query(20),
        db: Session = Depends(get_db)
):
    """获取词库"""
    from sqlalchemy import desc
    words = db.query(Word).filter(
        Word.difficulty == difficulty
    ).order_by(desc(Word.created_at)).offset(skip).limit(limit).all()

    return {
        "total": len(words),
        "words": [WordService.to_response_with_proficiency(db, w) for w in words]
    }


# ==================== 学习功能 ====================

@app.get("/api/study/random")
def get_random_word(
        difficulty: DifficultyLevel = Query(DifficultyLevel.CET4),
        exclude_id: int = Query(None, description="排除的单词ID，避免连续重复"),
        db: Session = Depends(get_db)
):
    """获取随机单词用于学习（优先未学过的）"""
    word = WordService.get_random_word(db, difficulty, exclude_id)

    if not word:
        raise HTTPException(status_code=404, detail="该难度等级暂无单词")

    return WordService.to_response_with_proficiency(db, word)


@app.post("/api/study/record")
def record_learning(
        word_id: int,
        data: LearningRecordUpdate,
        db: Session = Depends(get_db)
):
    """记录学习进度"""
    record = WordService.record_learning(db, word_id, data)
    return {"status": "success", "proficiency": record.proficiency}


# ==================== 统计分析 ====================

@app.get("/api/stats")
def get_stats(db: Session = Depends(get_db)):
    """获取学习统计"""
    return WordService.get_word_stats(db)


@app.get("/api/health")
def health():
    """健康检查"""
    return {"status": "ok", "message": "服务运行正常"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)