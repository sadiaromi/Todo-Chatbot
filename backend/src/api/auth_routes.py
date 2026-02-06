from fastapi import APIRouter, HTTPException, Depends, status, Header
from sqlmodel import Session
from typing import Dict
from datetime import datetime, timedelta
from src.services.database import get_session
from src.models.user import User, UserBase
from src.config import get_password_hash, verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from pydantic import BaseModel
from jose import JWTError
import uuid
from jose import jwt


router = APIRouter()


class UserRegister(BaseModel):
    email: str
    password: str
    username: str


class UserLogin(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


@router.post("/register")
def register(user_data: UserRegister, session: Session = Depends(get_session)):
    """Register a new user"""
    # Check if user already exists
    existing_user = session.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Validate password length (bcrypt limitation is 72 bytes)
    if len(user_data.password.encode('utf-8')) > 72:
        raise HTTPException(status_code=400, detail="Password cannot be longer than 72 bytes")

    # Create new user
    hashed_password = get_password_hash(user_data.password)
    db_user = User(
        email=user_data.email,
        username=user_data.username,
        password_hash=hashed_password
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(db_user.user_id)}, expires_delta=access_token_expires
    )

    return {
        "user_id": db_user.user_id,
        "email": db_user.email,
        "username": db_user.username,
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.post("/login")
def login(user_data: UserLogin, session: Session = Depends(get_session)):
    """Authenticate user and return access token"""
    # Validate password length (bcrypt limitation is 72 bytes)
    if len(user_data.password.encode('utf-8')) > 72:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Password cannot be longer than 72 bytes",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Find user by email
    db_user = session.query(User).filter(User.email == user_data.email).first()
    if not db_user or not verify_password(user_data.password, db_user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(db_user.user_id)}, expires_delta=access_token_expires
    )

    return {
        "user_id": str(db_user.user_id),
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.post("/verify")
def verify_token(token: str = Header(..., alias="Authorization")):
    """Verify if the token is valid and return user info"""
    try:
        # Remove Bearer prefix if present
        if token.startswith("Bearer "):
            token = token[7:]

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        # In a real app, you would fetch user details from DB
        # For now, just return basic user info
        return {"user_id": user_id}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")