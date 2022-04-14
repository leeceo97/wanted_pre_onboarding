
from .models import User


class JsonWebTokenMiddleWare(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        headers = request.headers
        username = headers.get("username", None)

        User.objects.get_or_create(email=username)
        response = self.get_response(request)

        return response