#  Copyright (c) 2021.
#  Developed by Mateusz Siga

from controller.controller import Controller
from controller.repository import Repository
from controller.service import Service
from utils.user_input import UserInput
from view.menu import Menu


class Application:

    def __init__(self):
        self.controller = Controller(Service(Repository()))

    def run(self):
        Menu.print_baner()
        exit_program = False
        while not exit_program:
            Menu.clear_screen()
            options = ['Add author', 'Add book', 'Show authors', 'Show books', 'Find authors', 'Find books']
            Menu.print_options('Select an option', options)
            option = UserInput.get_int('Type an option number', min=0, max=len(options))
            exit_program = self.go_to_section(option)

    def go_to_section(self, option):
        if option == 1:
            self.controller.add_author()
        if option == 2:
            self.controller.add_book()
        if option == 3:
            self.controller.show_authors()
        if option == 4:
            self.controller.show_books()
        if option == 5:
            self.controller.find_authors()
        if option == 6:
            self.controller.find_books()
        if option == 0:
            return True
        return False
