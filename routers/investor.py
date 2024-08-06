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

@router.get("/type", response_model=List[schemas.InvestorType])
def get_investor_types(db: Session = Depends(get_db)):
    investor_types = crud.get_investor_types(db)
    if not investor_types:
        raise HTTPException(status_code=404, detail="No investor types found")
    return investor_types

@router.get("/profile-investor-type", response_model=List[schemas.ProfileInvestorType])
def get_profile_investor_types(db: Session = Depends(get_db)):
    profile_investor_types = crud.get_profile_investor_types(db)
    if not profile_investor_types:
        raise HTTPException(status_code=404, detail="No profile investor types found")
    return profile_investor_types

@router.get("/profile-investor-type/{id}", response_model=List[schemas.InvestorType])
def get_profile_investor_type(id: str, db: Session = Depends(get_db)):
    investor_types = crud.get_profile_investor_type(db, user_id=id)
    if not investor_types:
        raise HTTPException(status_code=404, detail="No investor types found for this user")
    return investor_types
