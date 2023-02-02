from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('song.urls')),
    path('', include('album.urls')),
    path('', include('artist.urls')),
    path('', include('genre.urls')),
]
