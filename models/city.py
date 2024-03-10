#!/usr/bin/python3
"""
City class Module for AirBnB clone
"""


from models.base_model import BaseModel


class City(BaseModel):
    """City class for AirBnB clone"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """City class constructor

        Args:
            args: Variable length argument list
            kwargs: Arbitrary keyword arguments
        """
        super().__init__(*args, **kwargs)
