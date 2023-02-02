from django.db import models

from artist.models import Artist
from genre.models import Genre

class Album(models.Model):
    title = models.CharField(max_length=255)
    is_liked = models.BooleanField(default=False)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='albums',
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='albums',
    )

    def __str__(self) -> str:
        return self.title
