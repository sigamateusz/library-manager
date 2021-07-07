#  Copyright (c) 2021.
#  Developed by Mateusz Siga
import os

BANNER_PATH = './resources/banner.txt'


class Menu:

    @staticmethod
    def print_baner():
        os.system('cls')
        baner = open(BANNER_PATH, "r")
        print(baner.read())
        baner.close()
        Menu.press_enter()

    @staticmethod
    def press_enter():
        input('Press enter...')

    @staticmethod
    def clear_screen():
        os.system('cls')

    @staticmethod
    def print_section_name(section_name=''):
        Menu.clear_screen()
        print('-' * 50)
        print(' ' * 20 + section_name.upper())
        print('-' * 50)

    @staticmethod
    def warn(msg):
        print(f':::::{msg}:::::')
        Menu.press_enter()

    @staticmethod
    def print_options(title='', options=None):
        if options is None:
            options = []
        print(title)
        for idx, option in enumerate(options):
            print(f'{idx + 1}. {option}')
        print('0. EXIT')
