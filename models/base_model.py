#!/usr/bin/python3
"""
this is base model class
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    A base class that provides a unique identifier, timestamps
    for creation and update, and methods to save the object and
    convert it to a dictionary.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the object by setting the unique identifier and
        timestamps.
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k in ("created_at", "updated_at"):
                    setattr(self, k, datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the object.
        """
        ans = "[{}] ({}) {}".format(type(self).__name__,
                                    self.id, self.__dict__)
        return ans

    def save(self):
        """
        Updates the update timestamp.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Converts the object to a dictionary, with the option to format
        the timestamps as ISO 8601 strings.
        """
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                v = self.__dict__[k].isoformat()
                dic[k] = v
        return dic
