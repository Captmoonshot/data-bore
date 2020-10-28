from django import forms
from django.forms import ModelForm

from .models import Sentiment

class SentimentForm(forms.ModelForm):
	class Meta:
		models = Sentiment
		help_text = {
			"reviews": "Enter a short movie review"
		}
		fields = [
			"reviews",
		]

