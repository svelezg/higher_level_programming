#!/usr/bin/python3
"""
This is the "base" module.
It supplies one class, base.
"""

import json
import csv


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries:"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        my_list = []
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                return my_list
            else:
                for obj in list_objs:
                    my_list.append(obj.to_dictionary())
            f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        my_list = []
        if json_string is None or len(json_string) == 0:
            pass
        else:
            my_list = json.loads(json_string)
        return my_list

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy_instance = cls(1, 1, 0, 0)
        cls.update(dummy_instance, **dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        my_list = []
        result_list = []
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                list_input = f.read()
                list_output = cls.from_json_string(list_input)
                for elem in list_output:
                    my_object = cls.create(**elem)
                    result_list.append(my_object)
                return result_list
        except:
            return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """"serializes in CSV:"""
        filename = cls.__name__ + ".csv"
        aux = {}
        with open(filename, 'w') as f:
            header_list_rec = ['id', 'width', 'height', 'x', 'y']
            header_list_sq = ['id', 'size', 'x', 'y']
            if list_objs is None:
                return []
            else:
                if cls.__name__ == 'Rectangle':
                    writer = csv.DictWriter(f, fieldnames=header_list_rec)
                else:
                    writer = csv.DictWriter(f, fieldnames=header_list_sq)
                writer.writeheader()
                for obj in list_objs:
                    aux = obj.to_dictionary()
                    writer.writerow(aux)
                    # my_list.append(obj.to_dictionary())
            # f.write(cls.to_json_string(my_list))


    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        my_list = []
        result_list = []
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                list_output = csv.DictReader(f, delimiter=',')
                for elem in list_output:
                    print(elem)
                    print(type(elem))
                    print("1**************")
                    my_object = cls.create(**elem)
                    print("2**************")
                    print(my_object )
                    result_list.append(my_object)
                return result_list
        except:
            return my_list