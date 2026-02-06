from datetime import datetime, date
from sqlmodel import SQLModel, Field
from typing import Optional
import uuid


class TaskBase(SQLModel):
    title: str = Field(max_length=200)
    description: str = Field(default="", max_length=1000)
    status: str = Field(default="pending", sa_column_kwargs={"server_default": "pending"})
    priority: str = Field(default="medium", sa_column_kwargs={"server_default": "medium"})
    deadline: Optional[date] = Field(default=None)
    tags: Optional[str] = Field(default=None)  # JSON string


class Task(TaskBase, table=True):
    task_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="user.user_id")
    conversation_id: Optional[uuid.UUID] = Field(default=None, foreign_key="conversation.conversation_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = Field(default=None)

    # Validation constraints for status and priority
    __table_args__ = (
        {"sqlite_autoincrement": True},
    )