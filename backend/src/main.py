from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from .api.chat_routes import router as chat_router
from .api.auth_routes import router as auth_router
from .api.mcp_routes import router as mcp_router

load_dotenv()

app = FastAPI(title="Todo AI Chatbot API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/auth")  # Auth routes under /auth
app.include_router(chat_router, prefix="/api/{user_id}")  # Chat and task routes
app.include_router(mcp_router, prefix="")  # MCP tools routes without prefix

@app.get("/")
def read_root():
    return {"message": "Todo AI Chatbot API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}