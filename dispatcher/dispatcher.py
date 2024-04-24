import requests

from request.type import RequestType


class Dispatcher:

    def send(self, req):
        return self.get_sending_function(req)

    def get_sending_function(self, req):
        if req.rtype is RequestType.GET and req.payload is None:
            return self._get_all(req)
        elif req.rtype is RequestType.GET and req.payload is not None:
            return self._get_one(req)
        elif req.rtype is RequestType.POST:
            return self._create(req)
        elif req.rtype is RequestType.PUT:
            return self._update(req)
        elif req.rtype is RequestType.DELETE:
            return self._delete(req)

    def _get_all(self, req):
        return requests.get(req.url, auth=req.authentication).json()

    def _get_one(self, req):
        url = "{0}/{1}".format(req.url, req.payload)
        return requests.get(url, auth=req.authentication).json()

    def _create(self, req):
        return requests.post(req.url, data=req.payload, auth=req.authentication, headers=req.headers).json()

    def _update(self, req):
        return requests.put(req.url, data=req.payload, auth=req.authentication, headers=req.headers).json()

    def _delete(self, req):
        url = "{0}/{1}".format(req.url, req.payload)
        return requests.delete(url, auth=req.authentication).json()