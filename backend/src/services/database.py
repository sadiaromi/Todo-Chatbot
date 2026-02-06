from sqlmodel import create_engine, Session
from sqlalchemy.orm import sessionmaker
from typing import Generator
from dotenv import load_dotenv
import os

load_dotenv()

# Use SQLite for development, PostgreSQL for production
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo_chatbot.db")

# For SQLite, we need to add check_same_thread=False
if "postgresql" in DATABASE_URL.lower():
    engine = create_engine(DATABASE_URL, echo=True)
else:
    # Use SQLite
    engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()