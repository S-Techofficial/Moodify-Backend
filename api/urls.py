from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name="api.home"),
    path('category/', include('api.category.urls')),
    path('playlist/', include('api.playlist.urls')),
    path('song/', include('api.songs.urls')),
    path('user/', include('api.user.urls')),
    path('subscription/', include('api.subscription.urls')),
]
