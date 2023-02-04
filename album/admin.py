from django.contrib import admin

from .models import Album

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'genre']
    list_filter = ['artist', 'genre']
    list_editable = ['artist', 'genre']
