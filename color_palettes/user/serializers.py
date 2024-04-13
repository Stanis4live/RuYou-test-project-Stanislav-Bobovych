from rest_framework import serializers


class SignupSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()


class TokenSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
