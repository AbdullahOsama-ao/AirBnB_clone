#!/usr/bin/python3
"""
State class Module for AirBnB clone
"""


from models.base_model import BaseModel


class State(BaseModel):
    """State class for AirBnB clone"""
    name = ""

    def __init__(self, *args, **kwargs):
        """State class constructor

        Args:
            args: Variable length argument list
            kwargs: Arbitrary keyword arguments
        """
        super().__init__(*args, **kwargs)
