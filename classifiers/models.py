from django.db import models

class Sentiment(models.Model):
	reviews = models.TextField()
	results = models.CharField(max_length=12, null=True, blank=True)
	probabilities = models.FloatField(null=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

