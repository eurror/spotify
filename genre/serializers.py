from rest_framework import serializers

from .models import Genre
from album.models import Album
from album.serializers import AlbumSerializer
from song.models import Song
from song.serializers import SongSerializer

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['albums'] = AlbumSerializer(
            Album.objects.filter(genre=instance.pk), many=True
        ).data
        #TODO -> delete songs from album.songs
        representation['songs'] = SongSerializer(
            Song.objects.filter(genre=instance.pk), many=True
        ).data
        return representation
