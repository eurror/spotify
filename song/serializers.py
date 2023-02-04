from rest_framework import serializers

from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['genre'] = instance.genre.title
        representation['album'] = instance.album.title
        representation['artist'] = instance.artist.name
        return representation
