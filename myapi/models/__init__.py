import sys, inspect
from sqlalchemy import (
    Column, Integer
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer(), primary_key=True, autoincrement=True)

# import all models
from .Car import *
from .Person import *

def list_all_models():
    models = []
    ignore = ["Base", "BaseModel"]
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and hasattr(obj, "metadata"):
            if obj.__name__ not in ignore:
                models.append(obj)
    return models
