#  Copyright (c) 2021.
#  Developed by Mateusz Siga

class UserInput:

    @staticmethod
    def get_int(msg='', min=0, max=0):
        while True:
            try:
                user_input = int(input(f'{msg}: '))
                if min and user_input < min:
                    print('Too small number')
                    continue
                if max and user_input > max:
                    print('Too big number')
                    continue
                return user_input
            except ValueError:
                print("Wrong value, try again...")

    @staticmethod
    def get_str(msg, available_options=None):
        if available_options is None:
            available_options = []
        if len(available_options) == 0:
            return input(f'{msg}: ')

        str_options = []
        for option in available_options:
            str_options.append(str(option))

        while True:
            join = ", ".join(str_options)
            print(f'Available options: {join}')
            user_input = input(f'{msg}: ')
            if user_input in str_options:
                return user_input
