<!-- SYNC IMPACT REPORT:
Version change: N/A (initial) → 1.0.0
Added sections: All sections (initial constitution)
Removed sections: None
Modified principles: None (initial creation)
Templates requiring updates:
- ✅ .specify/templates/plan-template.md - updated to align with new principles
- ✅ .specify/templates/spec-template.md - updated to align with new principles
- ✅ .specify/templates/tasks-template.md - updated to align with new principles
Follow-up TODOs: None
-->
# Todo AI Chatbot Constitution

## Core Principles

### Statelessness by Design
All services must remain stateless; no in-memory storage of conversation or task state is permitted. All conversation context and task data must be persisted in the Neon Serverless PostgreSQL database. This ensures horizontal scalability and fault tolerance.

### Database-First Architecture
Neon Serverless PostgreSQL with SQLModel ORM serves as the single source of truth for all application data. All data operations must go through the database layer; direct in-memory state manipulation is prohibited.

### AI-Agent Isolation
AI agents using OpenAI Agents SDK must never access the database directly. AI agents may only interact with application state through MCP (Model Context Protocol) tools. This creates a clean separation of concerns and maintains architectural clarity.

### MCP-Only Data Access
MCP tools serve as the exclusive interface between AI agents and application data. These tools must be stateless and backed by the database. All business logic must be encapsulated within MCP tools to maintain consistency.

### Frontend-Separation
The Next.js frontend must not contain business logic or AI logic. The frontend is responsible solely for user interface presentation and interaction with backend APIs. All intelligent processing occurs on the backend.

### Technology Stack Adherence
The technology stack is fixed: Next.js frontend with OpenAI ChatKit for UI, Python FastAPI backend, OpenAI Agents SDK for AI logic, Neon Serverless PostgreSQL with SQLModel ORM for persistence, and Better Auth for authentication. Deviations require constitutional amendment.

## Additional Constraints

### Security Requirements
- All database connections must use SSL encryption
- Authentication via Better Auth must be enforced at the API gateway level
- No sensitive data should be logged in plain text
- MCP tools must implement proper authorization checks

### Performance Standards
- API response times must remain under 500ms for 95% of requests
- Database queries must utilize appropriate indexing
- Conversation history retrieval should be paginated to prevent memory bloat
- AI agent responses should have timeout mechanisms

### Deployment Policies
- Backend services must be deployable as containerized applications
- Database migrations must be version-controlled and reversible
- Environment-specific configurations must be managed through environment variables
- Feature flags must be implemented for safe rollouts

## Development Workflow

### Code Review Requirements
- All PRs must include database schema change documentation if applicable
- AI logic changes must include safety and reliability considerations
- MCP tool implementations must include comprehensive test coverage
- Frontend changes must maintain accessibility standards

### Testing Gates
- Unit tests must achieve 80% code coverage for backend services
- Integration tests must validate MCP tool functionality
- Database migration scripts must be tested in staging environment
- End-to-end tests must validate complete conversation flows

### Quality Assurance
- Static analysis tools must pass before merge
- Database schema changes require peer review
- AI agent behaviors must be validated for safety and correctness
- Performance benchmarks must be maintained or improved

## Governance

This constitution governs all development activities for the Todo AI Chatbot project. All team members must comply with these principles. Amendments to this constitution require explicit approval from project leadership and must include a migration plan for existing code. All pull requests and code reviews must verify compliance with these principles. Complexity must be justified with clear benefits outweighing the maintenance overhead. Use this document for runtime development guidance and decision-making.

**Version**: 1.0.0 | **Ratified**: 2026-01-18 | **Last Amended**: 2026-01-18