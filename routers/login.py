# routers/login.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from sql_app.crud import get_user_by_username, create_user
from sql_app.database import get_db
from sql_app.models import User
from auth import oauth2_scheme, get_current_active_user, create_access_token, pwd_context

router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = 30

@router.post("/token")
async def login_for_access_token(username: str, password: str, db: Session = Depends(get_db)):
    user = get_user_by_username(db, username)
    if not user or not pwd_context.verify(password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register")
async def register(username: str, password: str, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(password)
    new_user = create_user(db, username=username, password_hash=hashed_password)
    return new_user
