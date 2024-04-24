import unittest

import settings
from data.book import Book
from data.book_factory import BookFactory
from dispatcher.dispatcher import Dispatcher
from request.request import Request
from request.type import RequestType


class PostTests(unittest.TestCase):
    request = None
    dispatcher = None
    book = None

    @classmethod
    def setUp(cls):
        cls.book = BookFactory().fetch_book()
        cls.request = Request(type=RequestType.POST, headers={'Content-type': 'application/json'}, data=cls.book.to_json())
        cls.dispatcher = Dispatcher()

    def test_post(self):
        res = self.dispatcher.send(self.request)
        posted_book = Book(**res)
        self.assertIsNotNone(posted_book.id)


if __name__ == '__main__':
    unittest.main()
