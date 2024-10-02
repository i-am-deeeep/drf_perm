from rest_framework.response import Response
from .models import Movie
from drf_app.serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class MovieListAV(APIView):
    def get(self,request):
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class MovieDetailAV(APIView):
    def get(self,request,pk):
        try:
            movie=Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            movie=Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,pk):
        try:
            movie=Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        movie.delete()
