from django.urls import path

from .views import MovieAPIView, SentimentAPIView



urlpatterns = [
	path('movies', MovieAPIView.as_view()),
	path('sentiment', SentimentAPIView.as_view()),
]




