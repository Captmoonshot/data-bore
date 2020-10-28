from django.urls import path

from .views import classify_review, feedback

urlpatterns = [
	path('', classify_review, name='classify_review'),
	path('thanks', feedback, name='feedback'),
]