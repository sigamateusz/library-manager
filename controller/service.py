#  Copyright (c) 2021.
#  Developed by Mateusz Siga
import random
import string


class Service:

    def __init__(self, repo):
        self.repo = repo

    def add_author(self, author):
        saved = False
        while not saved:
            new_id = random.randint(1, 100)
            if self.find_author_by_id(new_id) is not None:
                continue
            author.set_id(new_id)
            self.repo.save_author(author)
            saved = True

    def add_book(self, book):
        saved = False
        while not saved:
            new_id = random.randint(1, 100)
            new_serial_number = self.generate_serial_number()
            if self.find_book_by_id(new_id) is not None and self.find_book_by_serial_number(new_serial_number) == '':
                continue
            book.set_id(new_id)
            book.set_serial_number(new_serial_number)
            self.repo.save_book(book)
            saved = True

    def get_authors(self):
        return tuple(self.repo.authors)

    def get_books(self):
        return tuple(self.repo.books)

    def find_author_by_id(self, idx):
        return next((author for author in self.repo.authors if author.get_id() == idx), None)

    def find_book_by_id(self, idx):
        return next((book for book in self.repo.books if book.get_id() == idx), None)

    def find_book_by_author_id(self, idx):
        return next((book for book in self.repo.books if book.get_author_id() == idx), None)

    def find_book_by_name(self, name):
        return next((book for book in self.repo.books if book.get_name() == name), None)

    def find_book_by_serial_number(self, serial_number):
        return next((book for book in self.repo.books if book.get_serial_number() == serial_number), '')

    def get_authors_ids(self):
        ids = []
        for author in self.repo.authors:
            ids.append(author.get_id())
        ids.sort()
        return ids

    def find_author_by_first_name(self, first_name):
        return next((author for author in self.repo.authors if author.get_first_name() == first_name), None)

    def find_author_by_last_name(self, last_name):
        return next((author for author in self.repo.authors if author.get_last_name() == last_name), None)

    def generate_serial_number(self):
        return self.random_letter() \
               + self.random_letter() \
               + '-' \
               + self.random_letter() \
               + self.random_letter() \
               + '-' \
               + self.random_letter() \
               + self.random_letter()

    @staticmethod
    def random_letter():
        letters = list(string.ascii_uppercase)
        return letters[random.randint(0, len(letters) - 1)]
