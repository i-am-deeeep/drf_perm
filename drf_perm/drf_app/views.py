from rest_framework.response import Response
from .models import Movie, Review
from drf_app.serializers import MovieSerializer, ReviewSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class MovieListAV(APIView):
    def get(self,request):
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies, many=True, context={'request':request})
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
        return Response(status=status.HTTP_204_NO_CONTENT)




class ReviewListAV(APIView):
    def get(self,request):
        reviews=Review.objects.all()
        serializer=ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class ReviewDetailAV(APIView):
    def get(self,request,pk):
        try:
            review=Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=ReviewSerializer(review)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            review=Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,pk):
        try:
            review=Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieReviewsAV(APIView):
    def get(self,request,pk):
        reviews=Review.objects.filter(movie=pk)
        serializer=ReviewSerializer(reviews,many=True)
        return Response(serializer.data)