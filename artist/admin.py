from django.contrib import admin

from .models import Artist

@admin.register(Artist)
class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name']
    list_filter = ['name', 'last_name']
    list_editable = ['last_name']
