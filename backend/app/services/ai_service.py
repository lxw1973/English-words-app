import openai
import json
import os
from app.schemas import DifficultyLevel
import random

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


class WordGenerator:
    """使用OpenAI生成单词及其信息"""

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        base_url = os.getenv("OPENAI_BASE_URL")
        if api_key:
            kwargs = {"api_key": api_key, "timeout": 60}
            if base_url:
                kwargs["base_url"] = base_url
            self.client = openai.OpenAI(**kwargs)
        else:
            # 未配置 OPENAI_API_KEY 时也允许服务正常启动，
            # AI 生成接口会回退到备用词库。
            self.client = None
            print("警告: 未设置 OPENAI_API_KEY，AI生成词库功能不可用，将使用备用词库")

    async def generate_word(self, difficulty: DifficultyLevel, db=None) -> dict:
        """生成一个单词的完整信息"""

        difficulty_prompts = {
            DifficultyLevel.CET4: "大学英语四级常考",
            DifficultyLevel.CET6: "大学英语六级常考",
            DifficultyLevel.BEC: "剑桥商务英语",
            DifficultyLevel.TOEFL: "托福考试",
            DifficultyLevel.IELTS: "雅思考试"
        }

        # 已存在的单词，用于提示模型避免重复
        exclude_words = ""
        if db is not None:
            from app.models import Word
            existing = db.query(Word.word).filter(
                Word.difficulty == difficulty
            ).all()
            if existing:
                exclude_words = "不要生成以下已存在的单词：" + "、".join([w[0] for w in existing][:80])

        prompt = f"""请生成一个{difficulty_prompts[difficulty]}的英语单词，返回JSON格式，包含以下字段：
        {{
            "word": "英文单词",
            "phonetic": "音标",
            "meaning": "中文意思（简要）",
            "definition": "英文定义（简要）",
            "example": "英文例句",
            "example_cn": "例句中文翻译",
            "pos": "词性(noun/verb/adj/adv等)"
        }}

        要求：
        1. 返回格式必须是有效的JSON
        2. 单词应该是实用的、常见的
        3. 例句应该简短易懂
        4. 不要返回markdown格式，直接返回JSON
        5. {exclude_words}
        """

        try:
            if self.client is None:
                raise RuntimeError("OPENAI_API_KEY 未配置，无法调用AI生成")
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7
            )

            # 解析返回的JSON（模型可能用 ```json 代码块包裹，需先清理）
            content = response.choices[0].message.content.strip()
            if content.startswith("```"):
                content = content.strip("`")
                if content.startswith("json"):
                    content = content[4:]
                content = content.strip()
            # 兼容直接返回带 ``` 的三引号包裹
            if content.startswith("```"):
                content = content.replace("```json", "").replace("```", "").strip()
            word_data = json.loads(content)
            word_data["difficulty"] = difficulty
            return word_data

        except Exception as e:
            print(f"AI生成失败: {e}")
            return self._generate_fallback_word(difficulty)

    def _generate_fallback_word(self, difficulty: DifficultyLevel) -> dict:
        """备用词库（如果AI失败）"""

        fallback_words = {
            DifficultyLevel.CET4: [
                {
                    "word": "persistent",
                    "phonetic": "/pəˈsɪstənt/",
                    "meaning": "持久的，顽强的",
                    "definition": "continuing firmly in an opinion or a course of action",
                    "example": "He has a persistent desire to succeed.",
                    "example_cn": "他有持久的成功欲望。",
                    "pos": "adj"
                },
                # ... 更多单词
            ],
            DifficultyLevel.CET6: [
                {
                    "word": "meticulous",
                    "phonetic": "/məˈtɪkjələs/",
                    "meaning": "细致的，谨慎的",
                    "definition": "showing great attention to detail",
                    "example": "Her meticulous research led to breakthrough discoveries.",
                    "example_cn": "她细致的研究导致了突破性发现。",
                    "pos": "adj"
                },
            ],
            # ... 其他难度
        }

        words = fallback_words.get(difficulty, fallback_words[DifficultyLevel.CET4])
        word = dict(random.choice(words))
        word["difficulty"] = difficulty
        return word