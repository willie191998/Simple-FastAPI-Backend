from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas
from typing import List

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.User])
def get_all_users(db: Session = Depends(get_db)):
    users = crud.get_all_users(db)
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users

@router.get("/{id}", response_model=schemas.User)
def get_user(id: str, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
