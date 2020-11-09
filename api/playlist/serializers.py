from rest_framework import serializers
from .models import Playlist


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = Playlist
        fields = ("id", 'name', 'description', 'category', 'image')
