from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from User.serializers import UserSerializer


class CreateUser(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserViewSet(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes =(JWTAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user
