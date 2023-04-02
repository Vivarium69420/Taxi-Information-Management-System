"""" A generic customer 
- id: unique id
- name: customer name
- phone_num: customer phone number
"""


class Customer:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__phone_num = None
        self.__chosen_vehicle = None

    def set_customer(self, id, name, phone_num, type):
        self.__id = id
        self.__name = name
        self.__phone_num = phone_num
        self.__chosen_vehicle = type

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_phone_num(self):
        return self.__phone_num

    def get_chosen_vehicle(self):
        return self.__chosen_vehicle
