#  Copyright (c) 2021.
#  Developed by Mateusz Siga

class Book:

    def __init__(self, author_id, name):
        self.author_id = author_id
        self.name = name
        self.id = 0
        self.serial_number = ''

    def set_id(self, idx):
        self.id = idx

    def set_serial_number(self, serial_number):
        self.serial_number = serial_number

    def get_author_id(self):
        return self.author_id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_serial_number(self):
        return self.serial_number

    def __str__(self):
        return f"ID:{self.id}|NAME:{self.name}|AUTHOR ID:{self.author_id}|SERIAL NUMBER:{self.serial_number}"
