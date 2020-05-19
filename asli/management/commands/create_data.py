from django.core.management.base import BaseCommand
from asli.models import Roznama, Category, Author 
import random
import datetime


categories = [
	'sport',
	'lifestyle',
	'music',
	'coding',
	'travelling',
]

authors = [
	'amir khan', 'shir', 'golnar','rana','rezagol','shagol','sidiqa','fatima','hassanyar','zahra','mohammadi','oranos'
]


def generate_author_name():
	index = random.randint(0,11)
	return authors[index]

def generate_category_name():
	index = random.randint(0,4)
	return categories[index]


def generate_view_count():
	return random.randint(0,100)

def generate_is_reviewed():
	val = random.randint(0,1)
	if val == 0:
		return False
	else:
		return True 

def generate_publish_date():
	year = random.randint(2000,2030)
	month = random.randint(1,12)
	day  = random.randint(1,28)
	return datetime.date(year,month,day)

class Command(BaseCommand):

	def add_arguments(self, parser):
		parser.add_argument('file_name',type=str, help="The txt file that contains the journal titles")

	def handle(self,*args, **kwargs):
		file_name = kwargs['file_name']
		with open(f'{file_name}.txt') as file :
			for row in file:
				title = row 
				author_name = generate_author_name()
				category_name = generate_category_name()
				publish_date = generate_publish_date()
				views = generate_view_count()
				reviewed = generate_is_reviewed()
				# print(title, author_name, category_name, publish_date, views, reviewed ,end="\n****\n")

				author = Author.objects.get_or_create(
						name = author_name
					)


				roznama = Roznama(
						title = title,
						author = Author.objects.get(name=author_name),
						publish_date = 	publish_date,
						views = views,
						reviewed = reviewed
					)
				roznama.save()


				category = Category.objects.get_or_create(
						name = category_name
					) 

				roznama.categories.add(
						Category.objects.get(name=category_name)
					)
		self.stdout.write(self.style.SUCCESS("Data imported successfuly"))
