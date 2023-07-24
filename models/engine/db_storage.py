#!/usr/bin/python3
"""
This module defines the DBStorage class which handles storage through
database using SQLAlchemy.
"""

from models.base_model import Base, BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv


class DBStorage:
    """
    This class handles storage through the database using SQLAlchemy.
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes the DBStorage instance.
        """
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of all objects of a specific class, if specified,
        otherwise, returns a dictionary of all objects.
        """
        from models import classes
        if cls is None:
            objs = self.__session.query(BaseModel).all()
            objs.update(self.__session.query(cls).all())
        else:
            if type(cls) == str and cls in classes:
                cls = classes[cls]
            objs = self.__session.query(cls).all()
        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in objs}

    def new(self, obj):
        """
        Adds an object to the current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the current database session if not None.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database and creates the current database
        session.
        """
        from models.state import State
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
        State.cities

