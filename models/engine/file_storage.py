#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "Amenity": Amenity,
                "City": City,
                "Review": Review,
                "State": State
                }


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
        for key, value in type(self).__objects.items():
            new_dict[key] = value.to_dict()
        with open(type(self).__file_path, "w", encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserializes the file to __objects if it exists"""
        try:
            with open(type(self).__file_path, "r", encoding='utf-8') as file:
                new_obj = json.load(file)
                for key, val in new_obj.items():
                    obj = class_dict[val['__class__']](**val)
                    type(self).__objects[key] = obj
        except FileNotFoundError:
            return
