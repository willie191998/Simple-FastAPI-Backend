from database import Base  # Absolute import
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = "profile"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    gender = Column(String, nullable=True)  # Allow gender to be nullable

class InvestorType(Base):
    __tablename__ = "investor_type"

    id = Column(Integer, primary_key=True, index=True)  # Ensure this is a String
    name = Column(String, unique=True, index=True)  # Specify a length of 255 characters

class ProfileInvestorType(Base):
    __tablename__ = "profile_investor_type"

    id = Column(Integer, primary_key=True, index=True)  # Assuming you change to Integer
    profile = Column(String, ForeignKey('profile.id'))  # Assuming User model has Integer ID
    investor_type = Column(Integer, ForeignKey('investor_type.id'))  # Assuming InvestorType model has Integer ID