from django.db import models

class Movie(models.Model):
	title = models.CharField(max_length=250)

	def __str__(self):
		return f"{self.title}"

class Sentiment(models.Model):
	reviews = models.TextField()
	results = models.CharField(max_length=12, null=True, blank=True)
	probabilities = models.FloatField(null=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

