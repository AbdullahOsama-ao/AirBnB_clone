#!/usr/bin/python3
"""
    BaseModel class Module for AirBnB clone
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class for AirBnB clone"""

    def __init__(self, *args, **kwargs):
        """BaseModel class constructor

        Args:
            args: Variable length argument list
            kwargs: Arbitrary keyword arguments
        """
        if kwargs:
            for atr in kwargs:
                if atr != "__class__":
                    if atr == "created_at" or atr == "updated_at":
                        setattr(self, atr, self.cnvrt_to_datetime(kwargs[atr]))
                    else:
                        setattr(self, atr, kwargs[atr])

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    @staticmethod
    def cnvrt_to_datetime(str):
        """Convert a string to a datetime object

        Args:
            str: String to convert

        Returns:
            datetime: Datetime object
        """
        return datetime.strptime(str, "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """Return a string representation of the BaseModel class

        Returns:
            str: String representation of the BaseModel class
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
        """Update the public instance attribute updated_at
        with the current datetime
        """
        models.storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel class

        Returns:
            dict: Dictionary representation of the BaseModel class
        """
        out = {}
        for el in self.__dict__:
            if el == "created_at" or el == "updated_at":
                out[el] = self.__dict__[el].strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                out[el] = self.__dict__[el]
        out["__class__"] = self.__class__.__name__
        return out
