#  Copyright (c) 2021.
#  Developed by Mateusz Siga

class Author:

    def __init__(self, first_name='', last_name=''):
        self.first_name = first_name
        self.last_name = last_name
        self.id = 0

    def set_id(self, idx):
        self.id = idx

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_id(self):
        return self.id

    def __str__(self):
        return f"ID:{self.id}|FIRST NAME:{self.first_name}|LAST NAME:{self.last_name}"
