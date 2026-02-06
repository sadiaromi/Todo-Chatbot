# Data Model: Todo AI Chatbot

## Overview
This document defines the database schema and entity relationships for the Todo AI Chatbot application, based on the entities identified in the feature specification.

## Entity Definitions

### User
Represents a registered user of the application.

**Fields:**
- `user_id`: UUID (Primary Key) - Unique identifier for the user
- `email`: String - User's email address (unique, indexed)
- `username`: String - User's display name (optional)
- `password_hash`: String - Hashed password (for basic auth)
- `created_at`: DateTime - Account creation timestamp
- `updated_at`: DateTime - Last account update timestamp
- `is_active`: Boolean - Whether the account is active

**Relationships:**
- One-to-Many with Conversation (user has many conversations)
- One-to-Many with Task (user has many tasks)

### Conversation
Represents a conversation session between the user and the AI assistant.

**Fields:**
- `conversation_id`: UUID (Primary Key) - Unique identifier for the conversation
- `user_id`: UUID (Foreign Key) - Reference to the owning user
- `title`: String - Auto-generated title based on first message
- `created_at`: DateTime - Conversation creation timestamp
- `updated_at`: DateTime - Last activity timestamp
- `status`: String - Current status (active, archived, pending)

**Relationships:**
- Many-to-One with User (belongs to user)
- One-to-Many with Message (conversation has many messages)

### Message
Represents a single message in a conversation.

**Fields:**
- `message_id`: UUID (Primary Key) - Unique identifier for the message
- `conversation_id`: UUID (Foreign Key) - Reference to the conversation
- `sender_type`: String - Who sent the message (user, assistant)
- `content`: Text - The actual message content
- `timestamp`: DateTime - When the message was sent
- `metadata`: JSON - Additional data about the message (tool calls, etc.)

**Relationships:**
- Many-to-One with Conversation (belongs to conversation)

### Task
Represents a todo item managed by the system.

**Fields:**
- `task_id`: UUID (Primary Key) - Unique identifier for the task
- `user_id`: UUID (Foreign Key) - Reference to the owner user
- `conversation_id`: UUID (Foreign Key, nullable) - Reference to conversation where task was created
- `title`: String - Task description
- `status`: String - Current status (pending, in-progress, complete, cancelled)
- `priority`: String - Priority level (low, medium, high, urgent)
- `deadline`: Date (nullable) - Due date for the task
- `created_at`: DateTime - Task creation timestamp
- `updated_at`: DateTime - Last update timestamp
- `completed_at`: DateTime (nullable) - When the task was completed
- `tags`: JSON (nullable) - Optional tags for categorization

**Relationships:**
- Many-to-One with User (belongs to user)
- Many-to-One with Conversation (optionally linked to conversation)

## Indexes

### Primary Indexes
- All primary keys are indexed by default

### Secondary Indexes
- `users.email` - For efficient user lookup during authentication
- `conversations.user_id` - For filtering conversations by user
- `conversations.updated_at` - For ordering conversations by recency
- `messages.conversation_id` - For retrieving messages in a conversation
- `messages.timestamp` - For chronological ordering of messages
- `tasks.user_id` - For filtering tasks by user
- `tasks.status` - For filtering tasks by status
- `tasks.priority` - For filtering tasks by priority
- `tasks.deadline` - For sorting and filtering by due date

## Relationships

```
Users 1 ---- * Conversations 1 ---- * Messages
Users 1 ---- * Tasks
Conversations 1 ---- * Messages
Conversations 0 ---- * Tasks (optional linkage)
```

## Validation Rules

### User
- Email must be a valid email format
- Email must be unique across all users
- Username must be 3-50 characters if provided
- Password must meet minimum strength requirements

### Conversation
- Title must be 1-100 characters
- Status must be one of: active, archived, pending
- Cannot belong to inactive user

### Message
- Content must be 1-10000 characters
- Sender type must be either 'user' or 'assistant'
- Must belong to an active conversation

### Task
- Title must be 1-200 characters
- Status must be one of: pending, in-progress, complete, cancelled
- Priority must be one of: low, medium, high, urgent
- Deadline cannot be in the past (validation at application level)
- Cannot belong to inactive user

## State Transitions

### Task Status Transitions
- `pending` → `in-progress` → `complete` (linear progression)
- `pending` → `cancelled` (direct cancellation)
- `in-progress` → `cancelled` (cancellation during work)
- `complete` → `in-progress` (reopening completed task)
- `cancelled` → `pending` (reactivating cancelled task)

### Conversation Status Transitions
- `active` → `archived` (manual archiving)
- `active` → `pending` (waiting for user response)
- `pending` → `active` (user resumes conversation)
- `archived` → `active` (user resumes archived conversation)

## Database Constraints

### Referential Integrity
- Foreign key constraints ensure data consistency
- Cascade deletion for conversations deletes associated messages
- Prevent orphaned records

### Uniqueness
- User emails must be unique
- No duplicate foreign key references where inappropriate

### Check Constraints
- Enum value validation for status and priority fields
- Date validation for deadline field (can be null or future date)
- Non-negative values where appropriate