from sqlmodel import Session, select
from typing import List, Optional
from datetime import datetime
import uuid
from ..models.conversation import Conversation, ConversationBase
from ..models.message import Message
from ..models.task import Task


class ConversationService:
    def __init__(self, session: Session):
        self.session = session

    def create_conversation(self, user_id: uuid.UUID, title: str = "") -> Conversation:
        """Create a new conversation for a user"""
        if not title:
            title = f"Conversation {datetime.now().strftime('%Y-%m-%d %H:%M')}"

        conversation = Conversation(user_id=user_id, title=title)
        self.session.add(conversation)
        self.session.commit()
        self.session.refresh(conversation)
        return conversation

    def get_user_conversations(
        self,
        user_id: uuid.UUID,
        limit: int = 20,
        offset: int = 0,
        sort_by: str = "updated_at",
        order: str = "desc"
    ) -> List[Conversation]:
        """Get conversations for a specific user"""
        query = select(Conversation).where(Conversation.user_id == user_id)

        # Apply sorting
        if sort_by == "updated_at":
            if order == "desc":
                query = query.order_by(Conversation.updated_at.desc())
            else:
                query = query.order_by(Conversation.updated_at.asc())
        elif sort_by == "created_at":
            if order == "desc":
                query = query.order_by(Conversation.created_at.desc())
            else:
                query = query.order_by(Conversation.created_at.asc())

        query = query.offset(offset).limit(limit)
        return self.session.execute(query).scalars().all()

    def get_conversation_by_id(self, conversation_id: uuid.UUID, user_id: uuid.UUID) -> Optional[Conversation]:
        """Get a specific conversation by ID for a user"""
        query = select(Conversation).where(
            Conversation.conversation_id == conversation_id,
            Conversation.user_id == user_id
        )
        return self.session.execute(query).scalar()

    def update_conversation_title(self, conversation_id: uuid.UUID, user_id: uuid.UUID, title: str) -> Optional[Conversation]:
        """Update a conversation title"""
        conversation = self.get_conversation_by_id(conversation_id, user_id)
        if not conversation:
            return None

        conversation.title = title
        conversation.updated_at = datetime.utcnow()

        self.session.add(conversation)
        self.session.commit()
        self.session.refresh(conversation)
        return conversation

    def get_conversation_messages(
        self,
        conversation_id: uuid.UUID,
        user_id: uuid.UUID,
        limit: int = 50,
        offset: int = 0
    ) -> List[Message]:
        """Get messages for a specific conversation"""
        # First verify the user owns this conversation
        conversation = self.get_conversation_by_id(conversation_id, user_id)
        if not conversation:
            return []

        query = select(Message).where(Message.conversation_id == conversation_id)
        query = query.order_by(Message.timestamp.asc()).offset(offset).limit(limit)
        return self.session.execute(query).scalars().all()

    def get_user_tasks_for_conversation(self, conversation_id: uuid.UUID, user_id: uuid.UUID) -> List[Task]:
        """Get tasks associated with a specific conversation"""
        # First verify the user owns this conversation
        conversation = self.get_conversation_by_id(conversation_id, user_id)
        if not conversation:
            return []

        query = select(Task).where(Task.conversation_id == conversation_id)
        return self.session.execute(query).scalars().all()