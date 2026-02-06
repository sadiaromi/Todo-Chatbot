from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional
import uuid


class MessageBase(SQLModel):
    sender_type: str = Field(sa_column_kwargs={"server_default": "user"})  # 'user' or 'assistant'
    content: str = Field(max_length=10000)
    metadata_json: Optional[str] = Field(default=None)  # JSON string


class Message(MessageBase, table=True):
    message_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    conversation_id: uuid.UUID = Field(foreign_key="conversation.conversation_id")
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    # Validation constraints for sender_type
    __table_args__ = (
        {"sqlite_autoincrement": True},
    )