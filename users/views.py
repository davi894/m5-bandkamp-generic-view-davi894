from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAccountOwner
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import User


class UserViewGenerics(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailViewGenerics(RetrieveUpdateDestroyAPIView, ListAPIView):
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    serializer_class = UserSerializer
