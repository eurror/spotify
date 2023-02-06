from rest_framework import serializers

from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.genre is not None:
            representation['genre'] = instance.genre.title
        if instance.album is not None:
            representation['album'] = instance.album.title
        if instance.artist is not None:
            representation['artist'] = instance.artist.name
        return representation
