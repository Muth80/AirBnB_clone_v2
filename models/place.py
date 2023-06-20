#!/usr/bin/python3
"""
Module: place
Defines the Place class, representing a place in the application.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """
    Place class representing a place in the application.

    Attributes:
        __tablename__ (str): Name of the table in the database.
        city_id (str): ID of the city associated with the place.
        user_id (str): ID of the user who owns the place.
        name (str): Name of the place.
        description (str): Description of the place.
        number_rooms (int): Number of rooms in the place.
        number_bathrooms (int): Number of bathrooms in the place.
        max_guest (int): Maximum number of guests allowed in the place.
        price_by_night (int): Price per night for the place.
        latitude (float): Latitude coordinate of the place.
        longitude (float): Longitude coordinate of the place.
        reviews (relationship): Relationship with the Review class.
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', cascade='all, delete', backref='place')

