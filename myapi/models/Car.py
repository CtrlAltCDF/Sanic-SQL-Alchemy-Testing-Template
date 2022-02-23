from sqlalchemy import (
    Column, String, ForeignKey
)

from sqlalchemy.orm import relationship

from myapi.models import BaseModel


class Car(BaseModel):
    __tablename__ = "car"

    brand = Column(String())
    user_id = Column(ForeignKey("person.id"))
    user = relationship("Person", back_populates="cars")
 