from django.urls import path

from . import views
from songs import views as song_views

urlpatterns = [
    path("albums/", views.AlbumViewGenerics.as_view()),
    path("albums/<int:pk>/songs/", song_views.SongsViewGenerics.as_view()),
]
