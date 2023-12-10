#!/usr/bin/python3
"""Contains the Review model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Implements the Review model.

    Fields:
    - place_id: A string representing the ID of the place associated with the review.
    - user_id: A string representing the ID of the user who created the review.
    - text: A string representing the content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes the review object.

        If keyword arguments are provided, it sets the corresponding attributes.
        Otherwise, it generates a new unique identifier, sets the creation and update timestamps, and saves the object.
        """
        super().__init__(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the review object.
        """
        return super().__str__()

    def save(self):
        """
        Updates the update timestamp and saves the review object.
        """
        super().save()

    def to_dict(self):
        """
        Converts the review object to a dictionary.

        Returns:
        - A dictionary representation of the review object.
        """
        return super().to_dict()
