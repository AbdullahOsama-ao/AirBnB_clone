#!/usr/bin/python3
"""
    FileStorage class Module for AirBnB clone
"""

import json
import os.path


class FileStorage:
    """FileStorage class for AirBnB clone"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """FileStorage class constructor"""
        pass

    def all(self):
        """ Method for all objects

        Returns:
            dict: __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """ Method for new objects

        Args:
            obj (obj): object to be saved
        """
        FileStorage.__objects["{}.{}".format(
            obj.__class__.__name__, obj.__dict__["id"])] = obj

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Method for Dictionary to JSON string

        Args:
            list_dictionaries (dict): dictionary to be converted

        Returns:
            str: JSON string
        """
        out_dict = {}

        if (list_dictionaries is None) or (list_dictionaries == "[]"):
            return "[]"

        for obj in list_dictionaries:
            out_dict[obj] = list_dictionaries[obj].to_dict()

        return json.dumps(out_dict)

    @staticmethod
    def from_json_string(json_string):
        """ Method for JSON string to Dictionary

        Args:
            json_string (str): JSON string to be converted

        Returns:
            dict: dictionary
        """
        if json_string is None or json_string == "[]":
            return {}
        else:
            return json.loads(json_string)

    def save(self):
        """ Method for saving objects to file """
        with open(FileStorage.__file_path, "w") as f:
            f.write(self.to_json_string(FileStorage.__objects))

    def reload(self):
        """ Method for reloading objects from file """
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        if os.path.exists(FileStorage.__file_path) is False:
            return

        with open(FileStorage.__file_path, "r") as f:
            objs_str = f.read()

        if objs_str is None or objs_str == "":
            return

        objs = self.from_json_string(objs_str)

        for k, v in objs.items():
            FileStorage.__objects[k] = eval(v["__class__"])(**v)
