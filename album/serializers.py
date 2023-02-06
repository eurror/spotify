from rest_framework import serializers

from .models import Album
from song.models import Song
from song.serializers import SongSerializer

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.artist is not None:
            representation['artist'] = instance.artist.name
        if instance.genre is not None:
            representation['genre'] = instance.genre.title
        representation['songs'] = SongSerializer(
            Song.objects.filter(album=instance.pk), many=True
        ).data
        return representation
