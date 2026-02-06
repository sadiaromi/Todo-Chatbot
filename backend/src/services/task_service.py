from sqlmodel import Session, select
from typing import List, Optional
from datetime import datetime
import uuid
from ..models.task import Task, TaskBase
from ..models.user import User


class TaskService:
    def __init__(self, session: Session):
        self.session = session

    def create_task(self, user_id: uuid.UUID, task_data: dict) -> Task:
        """Create a new task for a user"""
        # Create a Task object from the dictionary data
        task = Task(
            title=task_data.get('title', ''),
            description=task_data.get('description', ''),
            priority=task_data.get('priority', 'medium'),
            user_id=user_id
        )
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task

    def get_user_tasks(
        self,
        user_id: uuid.UUID,
        status_filter: str = "all",
        priority: Optional[str] = None,
        limit: int = 20,
        offset: int = 0
    ) -> List[Task]:
        """Get tasks for a specific user with optional filters"""
        query = select(Task).where(Task.user_id == user_id)

        if status_filter != "all":
            if status_filter == "pending":
                query = query.where(Task.status != "completed")
            elif status_filter == "completed":
                query = query.where(Task.status == "completed")

        if priority:
            query = query.where(Task.priority == priority)

        query = query.order_by(Task.created_at.desc()).offset(offset).limit(limit)
        return self.session.execute(query).scalars().all()

    def get_task_by_id(self, task_id: uuid.UUID, user_id: uuid.UUID) -> Optional[Task]:
        """Get a specific task by ID for a user"""
        query = select(Task).where(Task.task_id == task_id, Task.user_id == user_id)
        return self.session.execute(query).scalar()

    def update_task(self, user_id: uuid.UUID, task_id: uuid.UUID, update_data: dict) -> Optional[Task]:
        """Update a specific task for a user"""
        task = self.get_task_by_id(task_id, user_id)
        if not task:
            return None

        for key, value in update_data.items():
            if hasattr(task, key):
                setattr(task, key, value)
        task.updated_at = datetime.utcnow()

        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task

    def update_task_status(self, user_id: uuid.UUID, task_id: uuid.UUID, status: str) -> Optional[Task]:
        """Update the status of a specific task for a user"""
        task = self.get_task_by_id(task_id, user_id)
        if not task:
            return None

        task.status = status
        if status == "completed":
            task.completed_at = datetime.utcnow()
        else:
            task.completed_at = None
        task.updated_at = datetime.utcnow()

        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task

    def delete_task(self, user_id: uuid.UUID, task_id: uuid.UUID) -> bool:
        """Delete a specific task for a user"""
        task = self.get_task_by_id(task_id, user_id)
        if not task:
            return False

        self.session.delete(task)
        self.session.commit()
        return True