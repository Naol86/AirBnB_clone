#!/usr/bin/python3
"""
this is base model class
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    A base class that provides a unique identifier, timestamps
    for creation and update, and methods to save the object and
    convert it to a dictionary.
    """

    def __init__(self):
        """
        Initializes the object by setting the unique identifier and
        timestamps.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the object.
        """
        ans = "[{}}] ({}) <{}>".format(type(self).__name__,
                                       self.id, self.__dict__)
        return ans

    def save(self):
        """
        Updates the update timestamp.
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """
        Converts the object to a dictionary, with the option to format
        the timestamps as ISO 8601 strings.
        """
        dic = self.__dict__.copy()
        for i in self.__dict__:
            if i in {"created_at", "update_at"}:
                dic[i] = dic[i].isoformat()
        return dic
