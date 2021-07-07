#  Copyright (c) 2021.
#  Developed by Mateusz Siga

class Repository:

    def __init__(self):
        self.authors = []
        self.books = []

    def get_books(self):
        return self.books

    def get_authors(self):
        return self.authors.sort()

    def save_author(self, author):
        self.authors.append(author)

    def save_book(self, book):
        self.books.append(book)
