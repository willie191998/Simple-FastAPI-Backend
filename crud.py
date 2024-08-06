from sqlalchemy.orm import Session
import models, schemas

def get_all_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_investor_types(db: Session):
    return db.query(models.InvestorType).all()

def get_profile_investor_types(db: Session):
    return db.query(models.ProfileInvestorType).all()

def get_profile_investor_type(db: Session, user_id: str):
    return db.query(models.InvestorType).join(models.ProfileInvestorType).filter(models.ProfileInvestorType.profile == user_id).all()
