import json,os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jadeVine.settings')
import django
django.setup()
from jv.models import *

places = open("popular_places_87.json", "r")
category_file = open("categories.json", "r")
place_data = json.load(places)
category_data = json.load(category_file)

for category in category_data:
    new_category = Category()
    new_category.name = category["name"]
    new_category.imageUrl = category["img"]
    new_category.description = category["description"]
    new_category.save()

for place in place_data:
    new_place = Place()
    new_place.name = place["title"]
    new_place.description = place["description"]
    new_place.price = place["price"]
    new_place.imageUrl = place["image"]
    new_place.category = Category.objects.get(id= 1)
    new_place.save()