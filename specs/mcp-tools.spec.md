# MCP Tools Specification - Todo Management

## Overview
This document specifies the Model Context Protocol (MCP) tools that enable the AI agent to perform task management operations in a secure and controlled manner.

## Security Model
- **No Direct Database Access**: AI agents never access the database directly
- **Controlled Operations**: All data operations occur through predefined tools
- **User Isolation**: Each operation is scoped to the authenticated user
- **Stateless Operation**: Tools are stateless and operate on request basis

## Available Tools

### add_task
**Purpose**: Create a new task for the user

**Parameters**:
- `user_id` (string): UUID of the authenticated user
- `title` (string, required): Title of the task
- `description` (string, optional): Detailed description of the task
- `priority` (string, optional): Priority level (low, medium, high) - defaults to medium

**Returns**:
```json
{
  "success": true,
  "task_id": "uuid-string",
  "message": "Task 'title' added successfully",
  "task": {
    "id": "uuid-string",
    "title": "task title",
    "description": "task description",
    "completed": false,
    "priority": "medium",
    "created_at": "iso-date-string"
  }
}
```

### list_tasks
**Purpose**: Retrieve user's tasks with optional filtering

**Parameters**:
- `user_id` (string): UUID of the authenticated user
- `status` (string, optional): Filter by status (all, pending, completed) - defaults to all

**Returns**:
```json
{
  "success": true,
  "count": 5,
  "tasks": [
    {
      "id": "uuid-string",
      "title": "task title",
      "description": "task description",
      "completed": false,
      "priority": "medium",
      "created_at": "iso-date-string"
    }
  ]
}
```

### complete_task
**Purpose**: Mark a task as completed

**Parameters**:
- `user_id` (string): UUID of the authenticated user
- `task_id` (string): UUID of the task to complete

**Returns**:
```json
{
  "success": true,
  "message": "Task 'title' marked as completed",
  "task": {
    "id": "uuid-string",
    "title": "task title",
    "description": "task description",
    "completed": true,
    "priority": "medium",
    "updated_at": "iso-date-string"
  }
}
```

### update_task
**Purpose**: Update properties of an existing task

**Parameters**:
- `user_id` (string): UUID of the authenticated user
- `task_id` (string): UUID of the task to update
- `title` (string, optional): New title for the task
- `description` (string, optional): New description for the task
- `priority` (string, optional): New priority for the task

**Returns**:
```json
{
  "success": true,
  "message": "Task 'title' updated successfully",
  "task": {
    "id": "uuid-string",
    "title": "new task title",
    "description": "new task description",
    "completed": false,
    "priority": "high",
    "updated_at": "iso-date-string"
  }
}
```

### delete_task
**Purpose**: Remove a task from the user's list

**Parameters**:
- `user_id` (string): UUID of the authenticated user
- `task_id` (string): UUID of the task to delete

**Returns**:
```json
{
  "success": true,
  "message": "Task deleted successfully"
}
```

## Error Responses
All tools return a standardized error response format:
```json
{
  "success": false,
  "error": "error message",
  "message": "human-readable message"
}
```

## Implementation Requirements
- Tools must be stateless
- All database operations through SQLModel ORM
- Proper UUID validation for user and task IDs
- Comprehensive error handling and logging
- Transaction safety for data consistency