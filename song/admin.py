from django.contrib import admin

from .models import Song

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'album', 'genre']
    list_filter = ['artist', 'album', 'genre']
    list_editable = ['artist', 'album', 'genre']
