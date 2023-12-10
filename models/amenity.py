#!/usr/bin/python3
"""Contains the Amenity model"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity in a system.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
