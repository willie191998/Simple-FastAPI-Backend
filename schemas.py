from typing import List
from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    id: str
    name: str
    email: str
    gender: Optional[str]
class User(UserBase):
    id: str

    class Config:
        orm_mode: True
    
class InvestorTypeBase(BaseModel):
    id: int
    name: str
class InvestorType(InvestorTypeBase):
    id: int

    class Config:
        orm_mode: True

class ProfileInvestorTypeBase(BaseModel):
    id: int
    profile: str
    investor_type: int
class ProfileInvestorType(ProfileInvestorTypeBase):
    id: int

    class Config:
        orm_mode: True
