from sqlalchemy import (
    Column, String, ForeignKey
)

from sqlalchemy.orm import relationship

from myapi.models import BaseModel
from myapi.models.Car import Car


class Person(BaseModel):
    __tablename__ = "person"
    name = Column(String())
    cars = relationship(Car)

    def to_dict(self):
        return {"name": self.name, "cars": [{"brand": car.brand} for car in self.cars]}
