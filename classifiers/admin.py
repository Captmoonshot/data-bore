from django.contrib import admin

from .models import Sentiment


class SentimentAdmin(admin.ModelAdmin):
	class Meta:
		model = Sentiment
	list_display = [
		"id",
		"reviews",
		"results",
		"probabilities",
		"timestamp",
		"updated",
	]

admin.site.register(Sentiment, SentimentAdmin)


