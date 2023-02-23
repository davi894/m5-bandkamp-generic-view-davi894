from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
)
from django.urls import path


urlpatterns = [
    path('docs/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]