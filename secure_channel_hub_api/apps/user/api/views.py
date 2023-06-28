from django.contrib.auth import authenticate, login, get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions

from apps.user.api.serializers import RegistrationSerializer, UserSerializer
from common.utils.functions.utils import get_tokens_for_user


class RegisterView(APIView):
    User = get_user_model()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        password2 = request.data.get('password2')
        email = request.data.get('email')

        if not username or not password or not email or not password2:
            raise exceptions.ParseError('Credentials Missing')

        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            raise exceptions.ParseError('Required Fields Missing')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            user = UserSerializer(user)
            return Response({'message': 'Login Success', 'user': user.data, **auth_data},
                            status=status.HTTP_200_OK)
        raise exceptions.NotAuthenticated()
