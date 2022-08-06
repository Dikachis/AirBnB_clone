#!/usr/bin/python3

import json
from models.base_model import BaseModel


class FileStorage:
    """A class that serialize and deserialize instances to a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return type(self).__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, obj in type(self).__objects.items():
            new_dict[key] = obj.to_dict()
        with open(type(self).__file_path, "w", encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists"""
        try:
            with open(type(self).__file_path, encoding='utf-8') as file:
                for obj in json.load(file).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
