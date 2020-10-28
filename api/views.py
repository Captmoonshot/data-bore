from rest_framework import generics

from classifiers.models import Movie, Sentiment

from .serializers import MovieSerializer, SentimentSerializer



class MovieAPIView(generics.ListAPIView):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer

class SentimentAPIView(generics.ListAPIView):
	queryset = Sentiment.objects.all()
	serializer_class = SentimentSerializer



