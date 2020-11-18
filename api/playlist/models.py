from django.db import models
from api.category.models import Category
from api.user.models import CustomUser
# Create your models here.


class Playlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
