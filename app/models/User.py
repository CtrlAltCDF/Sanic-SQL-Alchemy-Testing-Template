from sqlalchemy import (
    Column, ForeignKey, String, Integer
)
from sqlalchemy.orm import (
    declarative_base,
    relationship
)

from .base import Base

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer(), primary_key=True, autoincrement=True)

class User(BaseModel):
    __tablename__ = "user"
    username = Column(String(), unique=True)
    usernamed = Column(String(), unique=True)