from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Genre
from .serializers import GenreSerializer

class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetailView(APIView):
    def get(self, request, pk):
        try:
            genre = Genre.objects.get(pk=pk)
            serializer = GenreSerializer(instance=genre)
            return Response(serializer.data, status=200)
        except Genre.DoesNotExist:
            return Response('This genre doesn\'t exist', status=404)
