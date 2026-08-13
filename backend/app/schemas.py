from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class DifficultyLevel(str, Enum):
    CET4 = "CET4"
    CET6 = "CET6"
    BEC = "BEC"
    TOEFL = "TOEFL"
    IELTS = "IELTS"

class WordResponse(BaseModel):
    id: int
    word: str
    phonetic: str
    meaning: str
    definition: str
    example: str
    example_cn: str
    difficulty: DifficultyLevel
    pos: str
    created_at: datetime
    proficiency: float = 0  # 熟练度 0-100，来自学习记录

    class Config:
        from_attributes = True

class WordCreate(BaseModel):
    word: str
    phonetic: str
    meaning: str
    definition: str
    example: str
    example_cn: str
    difficulty: DifficultyLevel
    pos: str

class LearningRecordUpdate(BaseModel):
    proficiency: float
    mark_as_learned: bool = False