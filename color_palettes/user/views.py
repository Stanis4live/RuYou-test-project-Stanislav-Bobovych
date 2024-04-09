from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SignupSerializer, TokenSerializer
from .services.login import authenticate_and_obtain_token

User = get_user_model()


class SignupAPIView(APIView):
    http_method_names = ['post']

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            name=serializer.validated_data['name']
        )
        token = authenticate_and_obtain_token(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        return Response(TokenSerializer(token).data, status=200)
