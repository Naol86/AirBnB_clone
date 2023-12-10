#!/usr/bin/python3
"""
this is file storage for my objects
"""
import json


class FileStorage:
    """
    A class responsible for storing objects in a file using
    JSON serialization and deserialization.

    Methods:
    - all(): Returns a dictionary containing all the objects in the storage.
    - new(obj): Adds a new object to the storage.
    - save(): Serializes the objects to JSON format and saves them to a file.
    - reload(): Deserializes the objects from a file and adds them to the
    storage.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary containing all the objects in the storage.

        Returns:
        - dict: A dictionary containing all the objects in the storage.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Parameters:
        - obj: The object to be added to the storage.
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serializes the objects to JSON format and saves them to a file.
        """
        with open(self.__file_path, "w") as file:
            dic = {}
            for k, v in self.__objects.items():
                dic[k] = v.to_dict()
            json.dump(dic, file)

    def reload(self):
        """
        Deserializes the objects from a file and adds them to the storage.
        """
        try:
            with open(self.__file_path, encoding="utf-8") as file:
                for obj in json.load(file).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
