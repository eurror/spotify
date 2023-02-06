from django.db import models

from album.models import Album
from artist.models import Artist
from genre.models import Genre

class Song(models.Model):
    title = models.CharField(max_length=60)
    duration = models.TimeField(blank=True, null=True)
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    paginate_by = 2
    image = models.ImageField(blank=True, null=True, upload_to='')
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='songs'
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='songs'
    )
    artist = models.ForeignKey(
        Artist,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='songs'
    )

    def __str__(self) -> str:
        return self.title
