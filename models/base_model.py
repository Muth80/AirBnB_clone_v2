from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid
from models import storage

Base = declarative_base()

class BaseModel:
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.__set_attributes(kwargs)
        if 'id' not in kwargs:
            self.id = str(uuid.uuid4())
        if 'created_at' not in kwargs:
            self.created_at = datetime.now()
        if 'updated_at' not in kwargs:
            self.updated_at = datetime.now()
        
    def __set_attributes(self, kwargs):
        for key, value in kwargs.items():
            if key != '__class__':
                setattr(self, key, value)
    
    def save(self):
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def delete(self):
        storage.delete(self)
        
    def to_dict(self):
        dictionary = dict(self.__dict__)
        dictionary.pop('_sa_instance_state', None)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

