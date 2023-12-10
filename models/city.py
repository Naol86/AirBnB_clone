#!/usr/bin/python3
"""Contains the City model"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city.

    Inherits the main functionalities and methods
    from the `BaseModel` class.

    Fields:
    - state_id: Represents the state ID of the city.
    - name: Represents the name of the city.
    """

    state_id = ""
    name = ""
