from django.urls import path

from .views import classify_review

urlpatterns = [
	path('', classify_review, name='classify_review'),
]