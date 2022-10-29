from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters

from account.renderers import UserRenderer
from .models import Song
from rest_framework import status
from .serializer import AllSongsListSerializer, SongSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class AllSongsListView(APIView):
    def get(self, request, format=None):
        songs = Song.objects.all()
        serializer=AllSongsListSerializer(songs, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class SongView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request,id, format=None):
        id=self.kwargs['id']
        song=Song.objects.get(id=id)
        serializer=SongSerializer(song)
        return Response(serializer.data,status=status.HTTP_200_OK)

        
        

class PostSongsView(APIView):
    def post(self,request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        
        
