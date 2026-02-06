# Quickstart Guide: Todo AI Chatbot

## Overview
This guide provides step-by-step instructions to set up and run the Todo AI Chatbot locally for development.

## Prerequisites
- Python 3.11+
- Node.js 18+
- Docker and Docker Compose (for database)
- OpenAI API key
- PostgreSQL client (for local development)

## Environment Setup

### 1. Clone the repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Set up backend environment
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up frontend environment
```bash
cd frontend
npm install
```

### 4. Configure environment variables
Create `.env` files in both backend and frontend directories:

**Backend (.env):**
```env
DATABASE_URL=postgresql://username:password@localhost:5432/todo_chatbot_dev
OPENAI_API_KEY=your_openai_api_key_here
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
NEON_DATABASE_URL=your_neon_database_url
```

**Frontend (.env.local):**
```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
NEXT_PUBLIC_OPENAI_DOMAIN_KEY=your_domain_key
```

## Database Setup

### 1. Start database with Docker
```bash
docker-compose up -d
```

### 2. Run database migrations
```bash
cd backend
source venv/bin/activate
alembic upgrade head
```

### 3. Initialize sample data (optional)
```bash
python -m src.scripts.initialize_sample_data
```

## Running the Application

### 1. Start the backend server
```bash
cd backend
source venv/bin/activate
uvicorn src.main:app --reload --port 8000
```

### 2. Start the MCP server (in a new terminal)
```bash
cd backend
source venv/bin/activate
python -m src.mcp_server.server
```

### 3. Start the frontend
```bash
cd frontend
npm run dev
```

### 4. Access the application
- Frontend: http://localhost:3000
- Backend API docs: http://localhost:8000/docs
- Backend API: http://localhost:8000/api

## Development Workflow

### Backend Development
1. Make changes to Python files
2. Server auto-reloads due to `--reload` flag
3. Run tests: `pytest tests/`
4. Format code: `black src/` and `isort src/`

### Frontend Development
1. Make changes to React components
2. Browser auto-refreshes
3. Run tests: `npm test`
4. Format code: `npm run format`

### Database Changes
1. Make model changes in `src/models/`
2. Generate migration: `alembic revision --autogenerate -m "description of changes"`
3. Review generated migration in `alembic/versions/`
4. Apply migration: `alembic upgrade head`

## Testing

### Run all tests
```bash
# Backend tests
cd backend
source venv/bin/activate
pytest tests/

# Frontend tests
cd frontend
npm test
```

### Run specific test suites
```bash
# Unit tests only
pytest tests/unit/

# Integration tests only
pytest tests/integration/

# Frontend component tests
npm test -- --watchAll=false
```

## API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login user
- `GET /auth/me` - Get current user info

### Chat
- `POST /api/{user_id}/chat` - Send message and get AI response
- `GET /api/{user_id}/conversations` - Get user's conversations
- `GET /api/{user_id}/conversations/{conversation_id}` - Get specific conversation

### Tasks
- `GET /api/{user_id}/tasks` - Get user's tasks
- `POST /api/{user_id}/tasks` - Create new task
- `PUT /api/{user_id}/tasks/{task_id}` - Update task
- `DELETE /api/{user_id}/tasks/{task_id}` - Delete task

## Troubleshooting

### Common Issues
1. **Database connection errors**: Verify PostgreSQL is running and credentials are correct
2. **API key errors**: Ensure OPENAI_API_KEY is set correctly in environment
3. **Port conflicts**: Check if ports 8000 or 3000 are already in use

### Resetting Development Environment
```bash
# Reset database
cd backend
alembic downgrade base
alembic upgrade head

# Clear frontend cache
cd frontend
rm -rf node_modules
npm install
```

## Production Deployment Notes
- Use environment variables for configuration
- Enable SSL for production
- Set up proper logging aggregation
- Configure health checks for containers