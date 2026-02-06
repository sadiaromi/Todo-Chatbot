# Todo AI Chatbot

## Description

A Todo AI Chatbot system that enables users to manage their tasks through natural language conversations. The system consists of a Next.js frontend with OpenAI ChatKit UI, a Python FastAPI backend, OpenAI Agents SDK for AI processing, and Neon Serverless PostgreSQL for data persistence. The system follows strict architectural principles including statelessness, database-first design, and AI-agent isolation.

## User Scenarios & Testing

### Scenario 1: Adding a new task
- **User**: "Add a task to buy groceries tomorrow"
- **System**: Recognizes intent to add task, extracts task details, confirms with user, and saves to database
- **Acceptance**: Task appears in user's todo list with correct details

### Scenario 2: Viewing pending tasks
- **User**: "Show me my pending tasks"
- **System**: Retrieves pending tasks from database and presents them in a readable format
- **Acceptance**: User sees all pending tasks with relevant details

### Scenario 3: Marking a task as complete
- **User**: "Mark the grocery task as complete"
- **System**: Identifies the specific task, updates status in database, confirms completion
- **Acceptance**: Task status changes to complete and is no longer shown in pending list

### Scenario 4: Resuming a conversation
- **User**: Returns to the application after leaving
- **System**: Loads previous conversation context using conversation_id
- **Acceptance**: User can continue the conversation where they left off

### Scenario 5: Editing or deleting tasks
- **User**: "Change the deadline for my project task to Friday" or "Delete the meeting note task"
- **System**: Processes edit/delete request, updates database, confirms changes
- **Acceptance**: Task is appropriately modified or removed from the system

## Functional Requirements

### FR1: Frontend Capabilities (Next.js + OpenAI ChatKit)
- The frontend must display chat interface allowing users to submit natural language messages
- The frontend must render AI responses in a readable format with appropriate styling
- The frontend must maintain conversation context using conversation_id across sessions
- The frontend must handle loading states during API communication with appropriate UI feedback
- The frontend must display error messages gracefully when API calls fail, with user-friendly explanations and recovery suggestions
- The frontend must use NEXT_PUBLIC_OPENAI_DOMAIN_KEY environment variable for domain allowlist configuration

### FR2: Chat API Service (FastAPI)
- The API must accept POST requests to /api/{user_id}/chat endpoint
- The API must accept optional conversation_id and required message in request body
- The API must return conversation_id, response text, and any tool_calls in response body
- The API must maintain statelessness with no in-memory conversation data
- The API must persist all conversations and messages to Neon Serverless PostgreSQL
- The API must authenticate requests using Better Auth before processing

### FR3: AI Agent Processing (OpenAI Agents SDK)
- The agent must detect natural language intents related to todo management (add, view, update, delete tasks)
- The agent must map detected intents to appropriate MCP tools for database operations
- The agent must support tool chaining for complex operations requiring multiple database calls
- The agent must never access the database directly, only through MCP tools
- The agent must maintain conversation context using the provided conversation_id
- The agent must generate human-friendly responses that confirm actions taken

### FR4: MCP Tools Interface
- MCP tools must provide database-backed operations for todo management (create, read, update, delete)
- MCP tools must be stateless and always retrieve current data from the database
- MCP tools must implement proper authorization checks to ensure data isolation between users (each user can only access their own data)
- MCP tools must return structured data that the AI agent can interpret and respond to users
- MCP tools must handle transaction management for operations that require consistency

### FR5: Database Operations (Neon Serverless PostgreSQL + SQLModel)
- The database must persist user accounts with authentication data
- The database must store conversation history with associated conversation_id
- The database must store todo items with status, priority, deadlines, and user associations
- The database must maintain referential integrity between users, conversations, and tasks
- The database must support efficient querying for common operations (pending tasks, recent conversations)
- The database must support filtering by status, priority, and date for task management

## Success Criteria

- 95% of user requests result in successful task management operations (add, view, update, delete)
- System responds to user messages within 3 seconds for 90% of requests
- Users can successfully resume conversations with their previous context intact
- Zero direct database access by AI agents (all access must be through MCP tools)
- System maintains full functionality during scaling events (stateless design validation)
- 99% uptime availability in production environment
- User satisfaction score of 4.0 or higher based on ease of use and task management effectiveness

## Key Entities

### User
- Unique identifier (user_id)
- Authentication credentials
- Profile information
- Preferences and settings

### Conversation
- Unique identifier (conversation_id)
- Associated user_id
- Timestamp of creation and last activity
- Status (active, archived)

### Message
- Unique identifier (message_id)
- Associated conversation_id
- Sender type (user, assistant)
- Content (text of the message)
- Timestamp

### Task/Todo Item
- Unique identifier (task_id)
- Associated user_id
- Task description
- Status (pending, in-progress, complete, cancelled)
- Priority level (low, medium, high, urgent)
- Deadline date
- Creation timestamp
- Completion timestamp
- (No recurring task support in initial implementation)

## Technical Context

The system follows a strict architectural pattern where:
- The frontend (Next.js) handles UI presentation only
- The backend (FastAPI) manages API requests and authentication
- The AI agent (OpenAI Agents SDK) processes natural language and orchestrates operations
- MCP tools provide database access and business logic
- The database (Neon Serverless PostgreSQL) stores all persistent data

All components maintain statelessness as required by the project constitution, with no in-memory storage of conversation or task state permitted.

## Assumptions

- Users have basic familiarity with chat interfaces
- Internet connectivity is available for all operations
- Better Auth provides sufficient authentication and authorization capabilities
- OpenAI Agents SDK supports the required natural language processing capabilities
- Neon Serverless PostgreSQL provides adequate performance and scalability
- Users access the system through modern web browsers

## Dependencies

- Next.js framework for frontend development
- OpenAI ChatKit for chat UI components
- Python FastAPI for backend API service
- OpenAI Agents SDK for AI processing
- Model Context Protocol (MCP) SDK for tool integration
- Neon Serverless PostgreSQL for data persistence
- SQLModel ORM for database modeling
- Better Auth for authentication
- Environment variables for configuration

## Clarifications

### Session 2026-01-18

- Q: What priority levels should be supported for tasks? → A: Low/Medium/High/Urgent priority levels
- Q: What authorization levels should be supported? → A: Basic user isolation only (each user can only access their own data)
- Q: What search and filtering capabilities should be available? → A: Basic filters by status, priority, and date
- Q: Should the system support recurring tasks? → A: No recurring tasks initially, focus on single-instance tasks
- Q: How should error handling and user notifications be approached? → A: Clear error messages with user-friendly explanations and recovery suggestions

## Out of Scope

- Mobile native applications (focus is on web-based chat interface)
- Offline functionality (requires internet connection)
- Third-party integrations (calendar, email, etc.) beyond core todo functionality
- Advanced analytics or reporting features
- Multi-language support beyond English
- Voice input/output capabilities