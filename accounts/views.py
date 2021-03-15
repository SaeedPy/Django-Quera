from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer



class LogoutAPIView(APIView):
    pass


class UserRegistration(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def post(self, request, *args, **kwargs):
    #     user_serializer = UserSerializer(data=request.data)
    #     if user_serializer.is_valid():
    #         user = user_serializer.save()
    #         if user:
    #             token = Token.objects.create(user=user)
    #             json = user_serializer.data
    #             json['token'] = token.key
    #         return Response(json, status=status.HTTP_201_CREATED)
    #     return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)