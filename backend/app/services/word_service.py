from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from app.models import Word, LearningRecord, DifficultyLevel
from app.schemas import WordCreate, LearningRecordUpdate, WordResponse
import random


class WordService:
    """单词业务逻辑"""

    @staticmethod
    def create_word(db: Session, word_data: WordCreate) -> Word:
        """创建单词"""
        # 检查是否已存在
        existing = db.query(Word).filter(Word.word == word_data.word).first()
        if existing:
            return existing

        db_word = Word(**word_data.dict())
        db.add(db_word)
        db.commit()
        db.refresh(db_word)
        return db_word

    @staticmethod
    def get_random_word(db: Session, difficulty: DifficultyLevel, exclude_id: int = None) -> Word:
        """获取随机单词：优先未学过的词，其次未完全掌握的，最后兜底随机；可排除指定词避免连续重复"""
        base = db.query(Word).filter(Word.difficulty == difficulty)
        if exclude_id is not None:
            base = base.filter(Word.id != exclude_id)

        # 1. 从未学过（无学习记录）
        unlearned = base.outerjoin(
            LearningRecord, Word.id == LearningRecord.word_id
        ).filter(LearningRecord.id.is_(None)).all()
        pool = unlearned
        if not pool:
            # 2. 学过但未完全掌握（proficiency < 100）
            pool = base.outerjoin(
                LearningRecord, Word.id == LearningRecord.word_id
            ).filter(
                LearningRecord.id.isnot(None),
                LearningRecord.proficiency < 100
            ).all()
        if not pool:
            # 3. 兜底：当前难度全部单词
            pool = base.all()

        if not pool:
            return None
        return random.choice(pool)

    @staticmethod
    def to_response_with_proficiency(db: Session, word: Word) -> dict:
        """将 Word 转为 WordResponse dict，并附加该词的学习熟练度"""
        data = WordResponse.from_orm(word).__dict__
        record = db.query(LearningRecord).filter(
            LearningRecord.word_id == word.id
        ).first()
        data["proficiency"] = record.proficiency if record else 0
        return data

    @staticmethod
    def get_word_stats(db: Session) -> dict:
        """获取学习统计"""
        total_words = db.query(func.count(Word.id)).scalar()

        stats_by_level = {}
        for level in DifficultyLevel:
            count = db.query(func.count(Word.id)).filter(
                Word.difficulty == level
            ).scalar()
            stats_by_level[level.value] = count

        return {
            "total_words": total_words,
            "by_difficulty": stats_by_level
        }

    @staticmethod
    def record_learning(db: Session, word_id: int, update_data: LearningRecordUpdate):
        """记录学习进度"""
        record = db.query(LearningRecord).filter(
            LearningRecord.word_id == word_id
        ).first()

        if not record:
            record = LearningRecord(word_id=word_id)
            db.add(record)

        record.times_learned = (record.times_learned or 0) + 1
        record.proficiency = update_data.proficiency

        if update_data.mark_as_learned:
            record.proficiency = 100

        db.commit()
        return record