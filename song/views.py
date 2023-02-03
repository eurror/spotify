from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from .models import Song
from .serializers import SongSerializer

class SongListView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetailView(APIView):
    def get(self, request, pk):
        try:
            song = Song.objects.get(pk=pk)
            serializer = SongSerializer(instance=song)
            return Response(serializer.data, status=200)
        except Song.DoesNotExist:
            return Response('This song doesn\'t exist', status=404)
