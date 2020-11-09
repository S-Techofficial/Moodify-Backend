from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.HyperlinkedModelSerializer):

    image = serializers.ImageField(
        max_length=None, allow_empty_file=True, allow_null=True, required=False)

    class Meta:
        model = Song
        fields = ("id","name", "artist", "album",
                  "image", "mood", "timeline", "playlist")
