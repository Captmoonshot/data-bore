from django.shortcuts import render

from .forms import SentimentForm
from .models import Sentiment

from .vectorizer import vect

import os
import pickle
import numpy as np




classifier = pickle.load(open(os.path.join('pkl_objects', 'classifier.pkl'), 'rb'))

def classify(reviews):
	label = {0: 'negative', 1: 'positive'}
	X = vect.transform([reviews])
	pred = classifier.predict(X)[0]
	proba = np.max(classifier.predict_proba(X))
	return label[pred], proba

def classify_review(request):
	form = SentimentForm(request.POST or None)
	if form.is_valid():
		reviews = form.cleaned_data.get("reviews")
		my_results, my_proba = classify(reviews)
		sentiment = Sentiment(reviews=reviews, results=my_results, probabilities=round(my_proba * 100, 2))
		sentiment.save()

		context = {
			'result': my_results,
			'probability': round(my_proba * 100, 2),
			'review': reviews,
		}
		return render(request, "classifiers/prediction.html", context)
	context = {
		"form": form,
	}
	return render(request, "classifiers/movie_classify.html", context)







