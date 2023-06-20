#!/usr/bin/python3
"""
Module: amenity
Defines the Amenity class, representing an amenity in the application.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """
    Amenity class representing an amenity in the application.

    Attributes:
        __tablename__ (str): Name of the table in the database.
        name (str): Name of the amenity.
        place_amenities (relationship): Relationship with the Place class through the place_amenity table.
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary='place_amenity', back_populates='amenities')

