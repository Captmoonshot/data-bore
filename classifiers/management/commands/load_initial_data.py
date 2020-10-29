import os
import csv
import time

from django.conf import settings

from data_bore_project.settings import DATABASES

from django.core.management.base import BaseCommand

from classifiers.models import Sentiment



db_name = DATABASES['default']['NAME']




def load_seed_data():
	with open(os.path.join('datasets', 'movie_and_demographic_data.csv'), 'r') as f:
		next(f)
		csv_reader = csv.reader(f)
		for row in csv_reader:
			sentiment = Sentiment(
				reviews=row[1],
				results=row[2],
				gender=row[3],
				age=row[4],
				country=row[5],
				movie_id=row[0]
			)
			sentiment.save()



class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		if settings.DEBUG:
			print(f"Seeding {db_name} database...")
		else:
			print(f"Seeding your production database...")
		time.sleep(2)
		load_seed_data()
		print("Done!")







