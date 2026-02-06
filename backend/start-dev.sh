#!/bin/bash

# Development startup script for Todo AI Chatbot backend

echo "Starting Todo AI Chatbot backend in development mode..."

# Install dependencies
pip install -r requirements.txt

# Run database migrations
alembic upgrade head

# Start the FastAPI server with auto-reload
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

echo "Backend server stopped."