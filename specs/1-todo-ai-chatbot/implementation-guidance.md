# Implementation Guidance: Todo AI Chatbot

## Overview
This document provides implementation guidance for developers working on the Todo AI Chatbot project. It follows the task breakdown in tasks.md and adheres to the architectural principles outlined in the constitution.

## Key Architecture Principles

### 1. Statelessness by Design
- No in-memory storage of conversation or task state
- All data must be persisted in Neon Serverless PostgreSQL
- Each request must retrieve necessary context from the database

### 2. AI-Agent Isolation
- OpenAI Agents SDK must never access the database directly
- All data access must go through MCP (Model Context Protocol) tools
- MCP tools must be stateless and database-backed

### 3. Frontend Separation
- Frontend handles only UI presentation
- No business logic or AI processing in the frontend
- All intelligent processing occurs on the backend

## Phase-by-Phase Implementation Guidance

### Phase 1: Setup (Shared Infrastructure)

#### T001: Create backend project structure
- **Technical Approach**: Set up FastAPI project with proper directory structure
- **Libraries/Frameworks**: FastAPI, uvicorn, python-dotenv
- **Key Responsibilities**: Initialize project with proper module organization
- **Integration Points**: N/A (foundational setup)
- **Common Mistakes**: Incorrect directory structure, missing dependencies
- **Validation Tips**: Verify basic FastAPI app runs successfully

#### T002: Create frontend project structure
- **Technical Approach**: Initialize Next.js project with ChatKit integration
- **Libraries/Frameworks**: Next.js, OpenAI ChatKit, axios/fetch
- **Key Responsibilities**: Set up basic routing and component structure
- **Integration Points**: N/A (foundational setup)
- **Common Mistakes**: Incorrect ChatKit configuration, missing dependencies
- **Validation Tips**: Verify basic Next.js app runs successfully

#### T003 [P]: Initialize Python virtual environment
- **Technical Approach**: Create and activate virtual environment, install dependencies
- **Libraries/Frameworks**: python -m venv, pip
- **Key Responsibilities**: Install FastAPI, SQLModel, OpenAI SDK, MCP SDK
- **Integration Points**: N/A (environment setup)
- **Common Mistakes**: Missing dependencies, incorrect Python version
- **Validation Tips**: Verify all required packages install correctly

#### T004 [P]: Initialize Node.js project
- **Technical Approach**: Create package.json, install Next.js and dependencies
- **Libraries/Frameworks**: npm/yarn, Next.js, react, openai-chatkit
- **Key Responsibilities**: Set up dependencies for frontend components
- **Integration Points**: N/A (environment setup)
- **Common Mistakes**: Version conflicts, missing peer dependencies
- **Validation Tips**: Verify all required packages install correctly

#### T005: Configure shared environment variables
- **Technical Approach**: Create .env files for both frontend and backend
- **Libraries/Frameworks**: python-dotenv, environment variable management
- **Key Responsibilities**: Define API keys, database URLs, configuration
- **Integration Points**: Used by both frontend and backend
- **Common Mistakes**: Exposing secrets in code, missing required variables
- **Validation Tips**: Verify environment variables are properly loaded

#### T006 [P]: Set up Docker configuration
- **Technical Approach**: Create docker-compose.yml for local development
- **Libraries/Frameworks**: Docker, docker-compose
- **Key Responsibilities**: Define services for backend, frontend, database
- **Integration Points**: Used for local development environment
- **Common Mistakes**: Incorrect port mappings, missing volumes
- **Validation Tips**: Verify all services start correctly

### Phase 2: Foundational (Blocking Prerequisites)

#### T007: Setup database schema and migrations
- **Technical Approach**: Configure SQLModel with Alembic for database migrations
- **Libraries/Frameworks**: SQLModel, Alembic, psycopg2-binary
- **Key Responsibilities**: Define base models, create migration framework
- **Integration Points**: Used by all data access layers
- **Common Mistakes**: Incorrect model definitions, missing indexes
- **Validation Tips**: Run migrations successfully, verify database schema

#### T008 [P]: Implement authentication framework
- **Technical Approach**: Integrate Better Auth for user authentication
- **Libraries/Frameworks**: Better Auth, JWT, bcrypt
- **Key Responsibilities**: Handle user registration/login, token management
- **Integration Points**: Protects all API endpoints
- **Common Mistakes**: Weak password hashing, token security issues
- **Validation Tips**: Test registration/login flows, verify token validation

#### T009 [P]: Setup API routing and middleware
- **Technical Approach**: Configure FastAPI routes and middleware
- **Libraries/Frameworks**: FastAPI, middleware components
- **Key Responsibilities**: Define route handlers, request/response processing
- **Integration Points**: Entry point for all API requests
- **Common Mistakes**: Incorrect middleware order, missing error handling
- **Validation Tips**: Test basic API endpoints, verify middleware functionality

#### T010: Create base models
- **Technical Approach**: Define SQLModel classes for core entities
- **Libraries/Frameworks**: SQLModel, Pydantic
- **Key Responsibilities**: Define User, Task, Conversation, Message models
- **Integration Points**: Used by services, API endpoints, MCP tools
- **Common Mistakes**: Incorrect relationships, missing validation
- **Validation Tips**: Verify model creation, relationship integrity

#### T011: Configure error handling and logging
- **Technical Approach**: Set up centralized error handling and logging
- **Libraries/Frameworks**: Python logging, FastAPI exception handlers
- **Key Responsibilities**: Handle exceptions, log operations consistently
- **Integration Points**: Used throughout the application
- **Common Mistakes**: Inconsistent error responses, missing log levels
- **Validation Tips**: Test error scenarios, verify log output

#### T012: Setup environment configuration
- **Technical Approach**: Create configuration management system
- **Libraries/Frameworks**: Pydantic settings, environment variables
- **Key Responsibilities**: Centralize configuration, validate settings
- **Integration Points**: Used by all application components
- **Common Mistakes**: Hardcoded values, missing validation
- **Validation Tips**: Verify configuration loading, validation errors

#### T013 [P]: Initialize MCP server structure
- **Technical Approach**: Set up MCP server with proper structure
- **Libraries/Frameworks**: Official MCP SDK, FastAPI
- **Key Responsibilities**: Define MCP server, tool registration
- **Integration Points**: Connects AI agents to backend services
- **Common Mistakes**: Incorrect tool definitions, connection issues
- **Validation Tips**: Verify MCP server starts, tools register correctly

#### T014 [P]: Initialize OpenAI Agents SDK
- **Technical Approach**: Configure agent framework with proper setup
- **Libraries/Frameworks**: OpenAI Agents SDK, configuration management
- **Key Responsibilities**: Set up agent configuration, tool integration
- **Integration Points**: Connects to MCP server for data access
- **Common Mistakes**: Incorrect API keys, tool configuration
- **Validation Tips**: Verify agent initialization, tool availability

#### T015: Create database connection utilities
- **Technical Approach**: Implement database session management
- **Libraries/Frameworks**: SQLModel, async session management
- **Key Responsibilities**: Handle database connections, session lifecycle
- **Integration Points**: Used by all data access operations
- **Common Mistakes**: Connection leaks, improper session handling
- **Validation Tips**: Test connection pooling, session management

### Phase 3: User Story 1 - Add and View Tasks (MVP)

#### T016 [P] [US1]: Contract test for chat endpoint
- **Technical Approach**: Create test that validates API contract
- **Libraries/Frameworks**: pytest, httpx for testing
- **Key Responsibilities**: Define expected request/response structure
- **Integration Points**: Validates chat endpoint functionality
- **Common Mistakes**: Insufficient test coverage, wrong expectations
- **Validation Tips**: Verify test fails before implementation, passes after

#### T017 [P] [US1]: Integration test for task creation
- **Technical Approach**: Test complete task creation flow
- **Libraries/Frameworks**: pytest, test database
- **Key Responsibilities**: Verify end-to-end task creation process
- **Integration Points**: Tests integration between components
- **Common Mistakes**: Mocking too much, not testing real flow
- **Validation Tips**: Verify complete flow works as expected

#### T018 [P] [US1]: Integration test for task retrieval
- **Technical Approach**: Test complete task retrieval flow
- **Libraries/Frameworks**: pytest, test database
- **Key Responsibilities**: Verify end-to-end task retrieval process
- **Integration Points**: Tests integration between components
- **Common Mistakes**: Mocking too much, not testing real flow
- **Validation Tips**: Verify complete flow works as expected

#### T019 [P] [US1]: Create User model
- **Technical Approach**: Define User model with required fields
- **Libraries/Frameworks**: SQLModel, Pydantic
- **Key Responsibilities**: Handle user data structure and validation
- **Integration Points**: Used by authentication, task assignment
- **Common Mistakes**: Missing required validations, incorrect relationships
- **Validation Tips**: Verify model creation and validation

#### T020 [P] [US1]: Create Task model
- **Technical Approach**: Define Task model with required fields
- **Libraries/Frameworks**: SQLModel, Pydantic
- **Key Responsibilities**: Handle task data structure and validation
- **Integration Points**: Used by services, MCP tools, API endpoints
- **Common Mistakes**: Missing required validations, incorrect relationships
- **Validation Tips**: Verify model creation and validation

#### T021 [P] [US1]: Create Conversation model
- **Technical Approach**: Define Conversation model with required fields
- **Libraries/Frameworks**: SQLModel, Pydantic
- **Key Responsibilities**: Handle conversation data structure and validation
- **Integration Points**: Used by chat functionality, MCP tools
- **Common Mistakes**: Missing required validations, incorrect relationships
- **Validation Tips**: Verify model creation and validation

#### T022 [P] [US1]: Create Message model
- **Technical Approach**: Define Message model with required fields
- **Libraries/Frameworks**: SQLModel, Pydantic
- **Key Responsibilities**: Handle message data structure and validation
- **Integration Points**: Used by chat functionality, MCP tools
- **Common Mistakes**: Missing required validations, incorrect relationships
- **Validation Tips**: Verify model creation and validation

#### T023 [US1]: Implement TaskService
- **Technical Approach**: Create service layer for task operations
- **Libraries/Frameworks**: SQLModel, async database operations
- **Key Responsibilities**: Handle business logic for task operations
- **Integration Points**: Used by API endpoints, MCP tools
- **Common Mistakes**: Mixing business logic with data access
- **Validation Tips**: Test all service methods individually

#### T024 [US1]: Implement ConversationService
- **Technical Approach**: Create service layer for conversation operations
- **Libraries/Frameworks**: SQLModel, async database operations
- **Key Responsibilities**: Handle business logic for conversation operations
- **Integration Points**: Used by API endpoints, MCP tools, agents
- **Common Mistakes**: Mixing business logic with data access
- **Validation Tips**: Test all service methods individually

#### T025 [US1]: Implement chat endpoint
- **Technical Approach**: Create API endpoint for chat functionality
- **Libraries/Frameworks**: FastAPI, request/response models
- **Key Responsibilities**: Handle chat requests, interact with agent
- **Integration Points**: Connects frontend to backend AI processing
- **Common Mistakes**: Blocking synchronous operations, poor error handling
- **Validation Tips**: Test with various message types and scenarios

#### T026 [US1]: Create task creation MCP tool
- **Technical Approach**: Implement MCP tool for creating tasks
- **Libraries/Frameworks**: Official MCP SDK, TaskService
- **Key Responsibilities**: Allow AI agent to create tasks in database
- **Integration Points**: Used by OpenAI agent to create tasks
- **Common Mistakes**: Direct database access, incorrect tool signature
- **Validation Tips**: Test tool functionality through agent

#### T027 [US1]: Create task retrieval MCP tool
- **Technical Approach**: Implement MCP tool for retrieving tasks
- **Libraries/Frameworks**: Official MCP SDK, TaskService
- **Key Responsibilities**: Allow AI agent to retrieve tasks from database
- **Integration Points**: Used by OpenAI agent to get tasks
- **Common Mistakes**: Direct database access, incorrect tool signature
- **Validation Tips**: Test tool functionality through agent

#### T028 [US1]: Configure agent to use task tools
- **Technical Approach**: Update agent configuration to include task tools
- **Libraries/Frameworks**: OpenAI Agents SDK, MCP tools
- **Key Responsibilities**: Configure agent to recognize and use task tools
- **Integration Points**: Connects agent to MCP tools
- **Common Mistakes**: Incorrect tool registration, missing capabilities
- **Validation Tips**: Test agent with task-related prompts

#### T029 [US1]: Implement basic chat UI component
- **Technical Approach**: Create chat interface using ChatKit
- **Libraries/Frameworks**: React, OpenAI ChatKit, axios/fetch
- **Key Responsibilities**: Handle user input, display responses
- **Integration Points**: Connects to backend chat API
- **Common Mistakes**: State management issues, API connection problems
- **Validation Tips**: Test sending and receiving messages

#### T030 [US1]: Connect frontend to backend API
- **Technical Approach**: Implement API client for backend communication
- **Libraries/Frameworks**: axios/fetch, API service wrapper
- **Key Responsibilities**: Handle HTTP requests to backend
- **Integration Points**: Connects frontend to backend services
- **Common Mistakes**: Error handling, request/response mapping
- **Validation Tips**: Test all API endpoints from frontend

#### T031 [US1]: Add validation and error handling
- **Technical Approach**: Implement comprehensive validation and error handling
- **Libraries/Frameworks**: Pydantic validation, FastAPI exception handlers
- **Key Responsibilities**: Validate input, handle errors gracefully
- **Integration Points**: Applied across all components
- **Common Mistakes**: Inconsistent validation, poor error messages
- **Validation Tips**: Test error scenarios, verify validation

#### T032 [US1]: Add logging for task operations
- **Technical Approach**: Implement logging for task-related operations
- **Libraries/Frameworks**: Python logging, structured logging
- **Key Responsibilities**: Log important operations and decisions
- **Integration Points**: Applied to task operations
- **Common Mistakes**: Too verbose or not informative enough
- **Validation Tips**: Verify logs are generated correctly

## Integration Points Between Components

### Frontend ↔ Backend
- API communication via HTTP requests
- Authentication tokens passed in headers
- JSON request/response format
- Error handling and status codes

### Backend ↔ MCP Server
- MCP protocol for tool communication
- Stateful connection for tool access
- Tool registration and discovery
- Request/response handling

### MCP Server ↔ Database
- Database operations through services
- Transaction management
- Connection pooling
- Query optimization

### Agent ↔ MCP Tools
- Natural language processing
- Intent recognition
- Tool selection and execution
- Response generation

## Common Pitfalls and Best Practices

### Statelessness Violations
- Store conversation context in database, not memory
- Retrieve user/session data from database for each request
- Avoid caching data in application memory

### AI-Agent Direct Database Access
- Never allow agents to access database directly
- All data access must go through MCP tools
- Validate that agents only use approved tools

### Security Considerations
- Sanitize all user inputs
- Validate authentication on all endpoints
- Protect against injection attacks
- Secure API keys and credentials

### Performance Optimization
- Use database indexes appropriately
- Implement pagination for large datasets
- Optimize queries with proper joins
- Cache responses where appropriate

## Testing Recommendations

### Unit Tests
- Test individual functions and methods
- Mock external dependencies
- Verify edge cases and error conditions

### Integration Tests
- Test component interactions
- Use test databases
- Verify complete workflows

### Contract Tests
- Validate API contracts
- Ensure backward compatibility
- Test request/response formats

### End-to-End Tests
- Test complete user journeys
- Verify frontend-backend integration
- Validate agent responses

## Validation Checklist

### Before Moving to Next Phase
- All tasks in current phase are complete
- All tests pass
- Code follows architectural principles
- Documentation is up to date

### Phase Completion Verification
- MVP functionality works independently
- No blocking dependencies remain
- Performance meets requirements
- Security requirements satisfied

## Next Steps
After completing each phase:
1. Verify all tasks are complete
2. Run all tests to ensure functionality
3. Validate against original requirements
4. Update documentation if needed
5. Move to next phase or proceed to production