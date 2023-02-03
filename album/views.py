from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from .models import Album
from .serializers import AlbumSerializer

class AlbumListView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetailView(APIView):
    def get(self, request, pk):
        try:
            album = Album.objects.get(pk=pk)
            serializer = AlbumSerializer(instance=album)
            return Response(serializer.data, status=200)
        except Album.DoesNotExist:
            return Response('This album doesn\'t exist', status=404)
