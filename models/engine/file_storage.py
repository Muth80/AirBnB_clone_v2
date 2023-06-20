#!/usr/bin/python3
""" Test delete feature
"""
from models.base_model import BaseModel
import json


class FileStorage:
    """ File storage class """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ Returns a dictionary of objects """
        if cls is None:
            return self.__objects
        else:
            filtered_objects = {}
            for obj_id, obj in self.__objects.items():
                if type(obj) == cls:
                    filtered_objects[obj_id] = obj
            return filtered_objects

    def new(self, obj):
        """ Sets an object to the __objects dictionary """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def delete(self, obj=None):
        """ Deletes an object from __objects if it exists """
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def save(self):
        """ Serializes __objects to the JSON file """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as file:
                deserialized_objects = json.load(file)
                for key, value in deserialized_objects.items():
                    class_name = value['__class__']
                    obj = eval(class_name + '(**value)')
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

