from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional
import uuid


class ConversationBase(SQLModel):
    title: str = Field(max_length=100)
    status: str = Field(default="active", sa_column_kwargs={"server_default": "active"})


class Conversation(ConversationBase, table=True):
    conversation_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="user.user_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Validation constraints for status
    __table_args__ = (
        {"sqlite_autoincrement": True},
    )