#!/usr/bin/python3
"""
Module: user
Defines the User class, representing a user in the application.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """
    User class representing a user in the application.

    Attributes:
        __tablename__ (str): Name of the table in the database.
        email (str): Email address of the user.
        password (str): Password of the user.
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
        places (relationship): Relationship with the Place class.
        reviews (relationship): Relationship with the Review class.
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship('Place', cascade='all, delete', backref='user')
    reviews = relationship('Review', cascade='all, delete', backref='user')

