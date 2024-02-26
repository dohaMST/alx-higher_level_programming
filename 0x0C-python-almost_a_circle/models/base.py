#!/usr/bin/python3
"""defining the class"""
import json

class Base:
    """representing the classe"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saving list of objects"""
        if list_objs is None:
            list_objs = []
        f_name = cls.__name__ + ".json"
        dict_list = []

        for obj in list_objs:
            if isinstance(obj, cls):
                dict_list.append(obj.to_dictionary())

        with open(f_name, "w") as file:
            jsonString = cls.to_json_string(dict_list)
            file.write(jsonString)

    @staticmethod
    def from_json_string(json_string):
        """ get from json file """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creating new instance"""
        if cls.__name__ == "Rectangle":
            new_ins = cls(1, 1)
        elif cls.__name__ == "Square":
            new_ins = cls(1)
        new_ins.update(**dictionary)
        return new_ins

    @classmethod
    def load_from_file(cls):
        """ loads from JSON file """
        f_name = cls.__name__ + ".json"
        inst_list = []
        try:
            with open(f_name, 'r', encoding='utf-8') as file:
                data = file.read()
                if data:
                    json_data = cls.from_json_string(data)
                    for x in json_data:
                        inst = cls.create(**x)
                        inst_list.append(inst)
            return inst_list
        except FileNotFoundError:
            return inst_list
