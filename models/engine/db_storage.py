#!/usr/bin/python3
"""
This module defines the DBStorage class for database storage.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{database}',
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        from models import classes
        objects = {}
        if cls:
            query = self.__session.query(classes[cls])
            for obj in query.all():
                key = "{}.{}".format(cls, obj.id)
                objects[key] = obj
        else:
            for cls in classes.values():
                query = self.__session.query(cls)
                for obj in query.all():
                    key = "{}.{}".format(cls.__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        self.__session.remove()

