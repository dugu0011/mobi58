#from _typeshed import Self
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token
from accounts.models import UserProfile 

class APIAuthentication(ModelBackend):
    def authenticate(self, request, token=None):
        # token = request.META.get('HTTP_APIKEY')
        # if token is None:
        #     token = request.GET.get('token')
        # if not token:
        #     return None
        try:
            token = Token.objects.get(key=token)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('no such user')    

        return token, None
