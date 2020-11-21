from rest_framework import viewsets
from .serializers import PlaylistSerializer
from .models import Playlist
from django.contrib.auth import get_user_model
from django.http import JsonResponse
# Create your views here.

    
class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all().order_by('id')
    serializer_class = PlaylistSerializer
