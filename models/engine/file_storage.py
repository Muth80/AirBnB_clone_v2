#!/usr/bin/python3
"""
FileStorage module
"""

class FileStorage:
    """
    FileStorage class
    """

    def delete(self, obj=None):
        """
        Deletes an object from __objects if it exists.

        Args:
            obj (BaseModel): The object to delete.

        Returns:
            None
        """
        if obj is None:
            return

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]
            self.save()

    def all(self, cls=None):
        """
        Returns a list of objects of a specific class.

        Args:
            cls (type): The class type to filter the objects.

        Returns:
            dict: A dictionary of objects of the specified class.
        """
        if cls is None:
            return self.__objects

        objects_by_cls = {}
        for key, obj in self.__objects.items():
            if isinstance(obj, cls):
                objects_by_cls[key] = obj
        return objects_by_cls

