#!/usr/bin/python3
""" base: contains class Base """
import json
class Base:
    """
    base class for the entire circle
    Attributes:
           __nb_objects (int)
           id (int)
    Methods:
           __init__()
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialised the class attributes.
        Args:
            id (int)
        """
        if not id == None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string rep of a list objs to a file
        Args:
            list_objs: a list of instances who inherits of base
        cls: Class
        """
        file_name = cls.__name__ + ".json"
        new_list = []

        if list_objs is None:
            with open(file_name, 'w', encoding="utf-8") as jsonFile:
                jsonFile.write(new_list)

        else:
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
            with open(file_name, "w", encoding="utf-8") as jsonFile:
                jsonFile.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
            """
            Returns the list of the JSON string representation json_string
            Args:
                json_string: A string representing a list of dictionaries
            """
            if json_string is None or len(json_string) == 0:
                new_list = []
                return new_list
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        Args:
           cls: class in which objects are instance
           dictionary: Double pointer to a dictionary
        """
        new_obj = cls(10, 10)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """
        Return a list of all instances
        Args:
            cls: Current class
        """
        fileName = cls.__name__ + ".json"
        try:
            with open(fileName, mode="w", encoding="utf-8") as jsonFile:
                content = cls.from_json_string(jsonFile.read())

        except:
            return []


        instance_list = []
        for instance in content:
            temp = cls.create(**instance)
            instance_list.append(temp)
        return instance_list
