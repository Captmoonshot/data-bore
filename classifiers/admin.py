from django.contrib import admin

from .models import Sentiment, Movie


class SentimentAdmin(admin.ModelAdmin):
	class Meta:
		model = Sentiment
	list_display = [
		"id",
		"movie",
		"reviews",
		"results",
		'gender',
		'age',
		'country',
		"timestamp",
		"updated",
	]

admin.site.register(Sentiment, SentimentAdmin)

class MovieAdmin(admin.ModelAdmin):
	class Meta:
		model = Movie
	list_display = [
		"id",
		"title",
	]

admin.site.register(Movie, MovieAdmin)



