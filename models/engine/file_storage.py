#!/usr/bin/python3
"""
This module defines the FileStorage class which handles serialization and
deserialization of JSON file data.
"""

import json


class FileStorage:
    """
    This class handles serialization and deserialization of JSON file data.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(data, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the file exists)
        """
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as file:
                data = json.load(file)
            from models.base_model import BaseModel
            from models.user import User
            # Add more imports for other classes if needed
            for key, value in data.items():
                class_name = value['__class__']
                obj = eval(class_name)(**value)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

