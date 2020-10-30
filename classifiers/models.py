from django.db import models

class Movie(models.Model):
	title = models.CharField(max_length=250)

	def __str__(self):
		return f"{self.title}"

class Sentiment(models.Model):
	GENDER_CHOICES = (
		('Male', 'Male'),
		('Female', 'Female'),
	)
	COUNTRY_CHOICES = (
		('United States of America', 'United States of America'),
		('Canada', 'Canada'),
		('Mexico', 'Mexico'),
		('Europe', 'Europe'),
		('Japan', 'Japan'),
		('South Korea', 'South Korea'),
	)
	movie 		= models.ForeignKey(Movie, null=True, blank=True, on_delete=models.SET_NULL)
	reviews 	= models.TextField(null=True, blank=True)
	results 	= models.IntegerField(null=True, blank=True)
	gender 		= models.CharField(null=True, blank=True, max_length=6, choices=GENDER_CHOICES)
	age 		= models.IntegerField(null=True, blank=True)
	country		= models.CharField(null=True, blank=True, max_length=24, choices=COUNTRY_CHOICES)
	timestamp 	= models.DateField(auto_now_add=True)
	updated 	= models.DateField(auto_now=True)

	class Meta:
		ordering = ['-timestamp', '-updated']








