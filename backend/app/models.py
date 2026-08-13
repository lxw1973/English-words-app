from sqlalchemy import Column, String, Text, Integer, DateTime, Float, Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()


class DifficultyLevel(str, enum.Enum):
    CET4 = "CET4"
    CET6 = "CET6"
    BEC = "BEC"
    TOEFL = "TOEFL"
    IELTS = "IELTS"


class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True)
    word = Column(String(100), unique=True, index=True)
    phonetic = Column(String(100))  # 音标
    meaning = Column(Text)  # 中文意思
    definition = Column(Text)  # 英文定义
    example = Column(Text)  # 例句
    example_cn = Column(Text)  # 例句中文翻译
    difficulty = Column(Enum(DifficultyLevel))
    pos = Column(String(20))  # 词性
    created_at = Column(DateTime, default=datetime.utcnow)


class LearningRecord(Base):
    __tablename__ = "learning_records"

    id = Column(Integer, primary_key=True)
    word_id = Column(Integer)
    times_learned = Column(Integer, default=0)  # 学过几次
    last_learned = Column(DateTime)
    proficiency = Column(Float, default=0)  # 熟练度 0-100
    created_at = Column(DateTime, default=datetime.utcnow)