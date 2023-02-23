from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from .permissions import IsAccountOwner
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)
from .models import User
import ipdb


class UserViewGenerics(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailViewGenerics(
    RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
):
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    serializer_class = UserSerializer
