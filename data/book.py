import json


class Book:
    id = 0
    name = None
    author = None
    publisher = None
    category = None
    pages = 0
    price = 0.00

    def __init__(self, id, name, author, publisher, category, pages, price):
        self.id = id
        self.name = name
        self.author = author
        self.publisher = publisher
        self.category = category
        self.pages = pages
        self.price = price

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)