#!/usr/bin/python3
"""Review class Module for AirBnB clone"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review class for AirBnB clone

    Attributes:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Review class constructor

        Args:
            args: Variable length argument list
            kwargs: Arbitrary keyword arguments
        """

        super().__init__(*args, **kwargs)
