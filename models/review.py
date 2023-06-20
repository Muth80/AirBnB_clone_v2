#!/usr/bin/python3
"""
Module: review
Defines the Review class, representing a review in the application.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """
    Review class representing a review in the application.

    Attributes:
        __tablename__ (str): Name of the table in the database.
        text (str): Text of the review.
        place_id (str): ID of the place associated with the review.
        user_id (str): ID of the user who created the review.
    """
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

