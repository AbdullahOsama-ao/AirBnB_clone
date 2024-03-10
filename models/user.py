#!/usr/bin/python3
"""
User class Module for AirBnB clone
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class for AirBnB clone"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """User class constructor

        Args:
            args: Variable length argument list
            kwargs: Arbitrary keyword arguments
        """
        super().__init__(*args, **kwargs)
