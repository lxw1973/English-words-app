from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
import os

# 使用SQLite，简单高效
DATABASE_URL = "sqlite:///./words.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建表
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()