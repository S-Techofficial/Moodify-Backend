from django.db import models
from api.playlist.models import Playlist
from django.core.validators import FileExtensionValidator

# Create your models here.

MOOD_CHOICES = (
    ("CHILL", "CHILL"),
    ("SAD", "SAD"),
    ("HAPPY", "HAPPY"),
    ("ANGRY", "ANGRY"),
    ("MOTIVATIONAL", "MOTIVATIONAL"),
    ("DEVOTIONAL", "DEVOTIONAL")
)

TIMELINE_OPTIONS = (
    ("2020's", "2020's"),
    ("2010's", "2010's"),
    ("2000's", "2000's"),
    ("1990's", "1990's"),
    ("1980's", "1980's"),
    ("1970's", "1970's")
)


class Song(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    playlist = models.ManyToManyField(Playlist)
    audio = models.FileField(upload_to="audio/", blank=True, validators=[FileExtensionValidator(
        ['.mp3', '.wav', '.ogg'])], help_text=("Allowed_type - .mp3, .wav, .ogg"))
    # audio = AudioField(upload_to="audio/", blank="True", ext_whitelist=(".mp3",".wav",".ogg"), help_text=("Allowed_type - .mp3, .wav, .ogg"))
    mood = models.CharField(
        max_length=50, choices=MOOD_CHOICES, default="RANDOM")
    timeline = models.CharField(
        max_length=50, choices=TIMELINE_OPTIONS, default="LATEST")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
