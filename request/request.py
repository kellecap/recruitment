from requests.auth import HTTPBasicAuth
import settings
from request.type import RequestType


class Request:

    def __init__(self, **kwargs):
        self.authentication = kwargs.get('auth', HTTPBasicAuth(settings.USER, settings.PASS))
        self.headers = kwargs.get('headers', None)
        self.payload = kwargs.get('data', None)
        self.rtype = kwargs.get('type', RequestType.GET)
        self.url = kwargs.get('url', settings.URL)

