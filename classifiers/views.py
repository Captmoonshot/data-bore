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

def train(review, y):
	X = vect.transform([review])
	classifier.partial_fit(X, [y])

def classify_review(request):
	form = SentimentForm(request.POST or None)
	if form.is_valid():
		reviews = form.cleaned_data.get("reviews")
		my_results, my_proba = classify(reviews)
		# sentiment = Sentiment(reviews=reviews, results=my_results, probabilities=round(my_proba * 100, 2))
		# sentiment.save()

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


def feedback(request):

	feedback = request.POST["feedback_button"]
	review = request.POST["review"]
	prediction = request.POST["result"]

	inv_label = {'negative': 0, 'positive': 1}
	y = inv_label[prediction]
	if feedback == 'Incorrect':
		y = int(not(y))
	train(review, y)
	sentiment = Sentiment(reviews=review, results=y)
	sentiment.save()
	context = {}
	return render(request, 'classifiers/thanks.html', context)







