from rest_framework import serializers

from classifiers.models import Movie, Sentiment


class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = (
			'title',
		)

class SentimentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sentiment
		fields = (
			'id',
			'reviews', 
			'results',
			'timestamp',
		)





