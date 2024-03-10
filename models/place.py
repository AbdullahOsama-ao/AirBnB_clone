#!/usr/bin/python3
"""
Place class Module for AirBnB clone
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """Place class for AirBnB clone

    Attributes:
    city_id: string - empty string: it will be the City.id
    user_id: string - empty string: it will be the User.id
    name: string - empty string
    description: string - empty string
    number_rooms: integer - 0
    number_bathrooms: integer - 0
    max_guest: integer - 0
    price_by_night: integer - 0
    latitude: float - 0.0
    longitude: float - 0.0
    amenity_ids: string list - empty list: will be list of Amenity.id later
    """
    name = ""
    description = ""
    city_id = ""
    user_id = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Place class constructor

        Args:
            args: Variable length argument list
            kwargs: Arbitrary keyword arguments
        """
        super().__init__(*args, **kwargs)
