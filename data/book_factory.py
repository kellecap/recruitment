import json
from random import randrange

import settings
from data.book import Book


class BookFactory:

    def __init__(self):
        self.books = []

    def load_books(self, path):
        with open(path, "r") as book_file:
            data = json.load(book_file)
            for d in data["books"]:
                book = Book(**d)
                self.books.append(book)

        return self.books

    def fetch_book(self):
        self.load_books(settings.BOOKS)
        index = randrange(0, len(self.books))
        return self.books[index]
