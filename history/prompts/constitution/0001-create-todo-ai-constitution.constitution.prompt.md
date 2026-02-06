---
id: 1
title: "Create Todo AI Constitution"
stage: constitution
date_iso: "2026-01-18"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "todo-ai-chatbot"
branch: "master"
user: "Claude Sonnet 4.5"
command: "/sp.phr"
labels: ["constitution", "todo-ai", "architecture", "principles"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - ".specify/memory/constitution.md"
tests_yaml:
  - "none"
---

# PHR-1: Create Todo AI Constitution

## Prompt Text

```
You are Spec-Kit Plus Constitution Writer.

Create a constitution.md for Phase III: Todo AI Chatbot.

System Context:
- Frontend is already initialized using Next.js (create-next-app)
- Frontend uses OpenAI ChatKit for chat UI
- Backend is built using Python FastAPI
- AI logic must use OpenAI Agents SDK
- Task operations are exposed via an MCP server using the Official MCP SDK
- Database is Neon Serverless PostgreSQL using SQLModel ORM
- Authentication is handled via Better Auth

Core Architectural Principles:
- The backend server must be fully stateless
- No in-memory conversation or task state is allowed
- All conversation context must be persisted in the database
- AI agents must never access the database directly
- AI agents may only interact with application state through MCP tools
- MCP tools must also be stateless and database-backed
- The frontend must not contain business logic or AI logic

AI & Tooling Rules:
- OpenAI Agents SDK is mandatory for agent orchestration
- MCP tools are the only mechanism
```

## Response Text

Created a comprehensive constitution.md file for the Todo AI Chatbot project that incorporates all specified architectural principles and requirements, including statelessness, database-first architecture, AI-agent isolation, MCP-only data access, frontend separation, and technology stack adherence.

## Outcome Impact

Successfully established foundational governance document outlining core principles, constraints, and development workflow for the Todo AI Chatbot project, ensuring architectural compliance and consistent development practices.

## Tests Summary

none

## Files Summary

- .specify/memory/constitution.md: Created complete constitution document with all required sections

## Next Prompts

none

## Reflection Note

Establishing clear architectural principles early in the project helps ensure consistent implementation and prevents architectural drift during development.

## Evaluation

**Failure modes observed:** None

**Next experiment to improve prompt quality:** N/A