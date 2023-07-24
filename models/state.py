#!/usr/bin/python3
"""
This module defines the State class.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """
    This class defines a State for the database.
    """

    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        name = ""

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """
            Returns a list of City objects from storage linked to the current State
            """
            from models import storage
            from models.city import City
            all_cities = storage.all(City)
            state_cities = []
            for city in all_cities.values():
                if city.state_id == self.id:
                    state_cities.append(city)
            return state_cities

