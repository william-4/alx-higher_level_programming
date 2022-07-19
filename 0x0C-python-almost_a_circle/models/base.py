 #!/usr/bin/python3
"""
This module defines a class called Base
"""
import json


class Base:
    """
    The base class for all other classes in this project
    """

    ''' private class attribute for number of objects'''
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance

        Args:
        id (int): id of a new Base instance
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """
        Returns the JSON representstion of the argument given
        """
        if list_dictionaries == None:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    ''' classmethod decorator takes the class of calling method as input'''
    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    def from_json_string(json_string):
        """
        Returns a python list of the JSON input
        """
        if json_string == None:
            return ([])
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all the attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """
        This method returns a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return ([])
