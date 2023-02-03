from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .models import Artist
from .serializers import ArtistSerializer

class ArtistListView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetailView(APIView):
    def get(self, request, pk):
        try:
            artist = Artist.objects.get(pk=pk)
            serializer = ArtistSerializer(instance=artist)
            return Response(serializer.data, status=200)
        except Artist.DoesNotExist:
            return Response('This artist doesn\'t exist', status=404)
