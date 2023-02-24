from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.generics import ListCreateAPIView
from .serializers import SongSerializer
from albums.models import Album
from django.shortcuts import get_object_or_404


class SongsViewGenerics(ListCreateAPIView):
    queryset = Song.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        album = get_object_or_404(Album, id=self.kwargs["pk"])
        serializer.save(album=album)
