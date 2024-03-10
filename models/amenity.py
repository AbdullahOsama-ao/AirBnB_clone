#!/usr/bin/python3
"""
Amenity class Module for AirBnB clone
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class for AirBnB clone"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Amenity class constructor

        Args:
            args: Variable length argument list
            kwargs: Arbitrary keyword arguments
        """
        super().__init__(*args, **kwargs)
