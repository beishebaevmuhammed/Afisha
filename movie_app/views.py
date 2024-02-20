from django.forms import models
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializer, models

@api_view(['GET'])
def directors(request):
    director = models.Director.objects.all()
    data = serializer.DirectorSerializer(director, many=True).data
    return Response(data=data)

@api_view(['GET'])
def directors_detail_view(request, id):
    try:
        director_id = models.Director.objects.get(id=id)
    except models.Director.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND, data={'message': 'Director not found'})
    data = serializer.DirectorSerializer(director_id).data
    return Response(data=data)


@api_view(['GET'])
def movies(request):
    movie = models.Movie.objects.all()
    data = serializer.MovieSerializer(movie, many=True).data
    return Response(data=data)

@api_view(['GET'])
def movies_detail_view(request, id):
    try:
        movie_id = models.Movie.objects.get(id=id)
    except models.Movie.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND, data={'message': 'Director not found'})
    data = serializer.MovieSerializer(movie_id).data
    return Response(data=data)


@api_view(['GET'])
def reviews(request):
    review = models.Review.objects.all()
    data = serializer.ReviewSerializer(review, many=True).data
    return Response(data=data)

@api_view(['GET'])
def reviews_detail_view(request, id):
    try:
        review_id = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND, data={'message': 'Director not found'})
    data = serializer.ReviewSerializer(review_id).data
    return Response(data=data)