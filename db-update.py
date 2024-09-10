import json,os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jadeVine.settings')
import django
django.setup()
from jv.models import *

#open the files
places = open("popular_places_87.json", "r")
category_file = open("categories.json", "r")
picture_file = open("pictures.json", "r")

#load the data from the files
pictures = json.load(picture_file)
place_data = json.load(places)
category_data = json.load(category_file)


##update the database with the new data
#uncomment code bits as required

#category updates
for category in category_data:
    new_category = Category()
    new_category.name = category["name"]
    new_category.imageUrl = category["img"]
    new_category.description = category["description"]
    new_category.save()

#place updates
for place in place_data:
    new_place = Place()
    new_place.name = place["title"]
    new_place.description = place["description"]
    new_place.price = place["price"]
    new_place.imageUrl = place["image"]
    new_place.category = Category.objects.get(id= 1)
    new_place.save()

#picture updates
for picture in pictures:
    place = Place.objects.get(name=picture["title"] )
    for image in picture["images"]:
        #check if the image already exists
        if Place_Image.objects.filter(image_url=image).exists():
            continue
        new_picture = Place_Image()
        new_picture.place = place
        new_picture.image_url = image
        new_picture.caption = picture["title"]
        new_picture.save()