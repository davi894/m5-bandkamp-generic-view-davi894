from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from .serializers import SongSerializer
from albums.models import Album
from django.shortcuts import get_object_or_404
import ipdb


class SongsViewGenerics(ListAPIView, CreateAPIView):
    queryset = Song.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        album = get_object_or_404(Album, id=self.kwargs["pk"])
        serializer.save(album=album)
