from rest_framework.authentication import BaseAuthentication
from accounts.models import User


class JSONWebTokenAuthentication(BaseAuthentication):

    def authenticate(self, request):

        headers = request.headers
        username = headers.get("username", None)

        user = User.objects.get(email=username)
        return (user, None)