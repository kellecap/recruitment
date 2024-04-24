import unittest

from dispatcher.dispatcher import Dispatcher
from request.request import Request
from request.type import RequestType


class GetTests(unittest.TestCase):

    request = None
    dispatcher = None

    @classmethod
    def setUp(cls):
        cls.request = Request(type=RequestType.GET)
        cls.dispatcher = Dispatcher()

    def test_get_all(self):
        res = self.dispatcher.send(self.request)
        self.assertIsNotNone(res)


if __name__ == '__main__':
    unittest.main()
