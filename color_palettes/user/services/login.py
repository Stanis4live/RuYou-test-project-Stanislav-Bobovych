from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers


def authenticate_and_obtain_token(username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        update_last_login(None, user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    else:
        raise serializers.ValidationError('Invalid credentials')

