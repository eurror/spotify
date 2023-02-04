from rest_framework import serializers

from .models import Artist
from song.serializers import SongSerializer
from song.models import Song
from album.serializers import AlbumSerializer
from album.models import Album
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['songs'] = SongSerializer(
            Song.objects.filter(artist=instance.pk), many=True
        ).data
        representation['albums'] = AlbumSerializer(
            Album.objects.filter(artist=instance.pk), many=True
        ).data
        return representation
