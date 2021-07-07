#  Copyright (c) 2021.
#  Developed by Mateusz Siga
from prettytable import PrettyTable

from model.Author import Author
from model.Book import Book
from utils.user_input import UserInput
from view.menu import Menu


def is_list_defined(data, msg):
    if len(data) == 0:
        Menu.warn(msg)
        return False
    return True


class Controller:

    def __init__(self, service):
        self.service = service

    def add_author(self):
        Menu.print_section_name('add author')
        first_name = UserInput.get_str('Author first name')
        last_name = UserInput.get_str('Author last name')
        author = Author(first_name, last_name)
        self.service.add_author(author)
        Menu.press_enter()

    def add_book(self):
        Menu.print_section_name('add book')
        authors_ids = self.service.get_authors_ids()
        if not is_list_defined(authors_ids, 'You cannot add a book. There is no books yet'):
            return
        author_id = UserInput.get_str('Author id', authors_ids)
        name = UserInput.get_str('Book name')
        book = Book(int(author_id), name)
        self.service.add_book(book)
        Menu.press_enter()

    def show_authors(self):
        Menu.print_section_name('show authors')
        authors = self.service.get_authors()
        if not is_list_defined(authors, 'There is no authors yet'):
            return
        table = PrettyTable()
        table.field_names = ["ID", "FIRST NAME", "LAST NAME"]
        for author in authors:
            table.add_row([author.get_id(), author.get_first_name(), author.get_last_name()])
        print(table)
        Menu.press_enter()

    def show_books(self):
        Menu.print_section_name('show books')
        books = self.service.get_books()
        if not is_list_defined(books, 'There is no books yet'):
            return
        table = PrettyTable()
        table.field_names = ["ID", "AUTHOR ID", "BOOK NAME", "SERIAL NUMBER"]
        for book in books:
            table.add_row([book.get_id(), book.get_author_id(), book.get_name(), book.get_serial_number()])
        print(table)
        Menu.press_enter()

    def find_authors(self):
        Menu.print_section_name('Find authors')
        if not is_list_defined(self.service.get_authors(), 'There is no authors yet'):
            return
        options = ['By first name', 'By last name', 'By id']
        Menu.print_options('How do you want to search', options)
        selected_option = UserInput.get_int('Type option numer', min=1, max=len(options))
        if selected_option == 1:
            self.find_author_by_first_name()
        if selected_option == 2:
            self.find_author_by_last_name()
        if selected_option == 3:
            self.find_author_by_id()
        if selected_option == 0:
            return

    def find_author_by_first_name(self):
        first_name = UserInput.get_str('Type author first name')
        author = self.service.find_author_by_first_name(first_name)
        if author is None:
            Menu.warn(f'There is no authors with first name {first_name}')
        else:
            print(author)
            Menu.press_enter()

    def find_author_by_last_name(self):
        last_name = UserInput.get_str('Type author last name')
        author = self.service.find_author_by_last_name(last_name)
        if author is None:
            Menu.warn(f'There is no authors with last name {last_name}')
        else:
            print(author)
            Menu.press_enter()

    def find_author_by_id(self):
        idx = UserInput.get_int('Type author id', min=1)
        author = self.service.find_author_by_id(idx)
        if author is None:
            Menu.warn(f'There is no authors with id {idx}')
        else:
            print(author)
            Menu.press_enter()

    def find_books(self):
        Menu.print_section_name('Find books')
        if not is_list_defined(self.service.get_authors(), 'There is no books yet'):
            return
        options = ['By id', 'By name', 'By author id']
        Menu.print_options('How do you want to search', options)
        selected_option = UserInput.get_int('Type option numer', min=1, max=len(options))
        if selected_option == 1:
            self.find_book_by_id()
        if selected_option == 2:
            self.find_book_by_name()
        if selected_option == 3:
            self.find_book_by_author_id()
        if selected_option == 0:
            return

    def find_book_by_id(self):
        idx = UserInput.get_int('Type book id', min=1)
        book = self.service.find_book_by_id(idx)
        if book is None:
            Menu.warn(f'There is no books with id {idx}')
        else:
            print(book)
            Menu.press_enter()

    def find_book_by_name(self):
        name = UserInput.get_str('Type book name')
        book = self.service.find_book_by_name(name)
        if book is None:
            Menu.warn(f'There is no books with name {name}')
        else:
            print(book)
            Menu.press_enter()

    def find_book_by_author_id(self):
        idx = UserInput.get_int('Type author id', min=1)
        book = self.service.find_book_by_author_id(idx)
        if book is None:
            Menu.warn(f'There is no books with author id {idx}')
        else:
            print(book)
            Menu.press_enter()
