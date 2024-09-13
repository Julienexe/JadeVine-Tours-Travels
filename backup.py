import json,os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jadeVine.settings')
import django
django.setup()
from jv.models import *

#open the files
place_file = open("popular_places_87.json", "w")
#category_file = open("categories.json", "w")
#picture_file = open("pictures.json", "w")

#load data from the database
categories = Category.objects.all()
places = Place.objects.all()
pictures = Place_Image.objects.all()

#write the data to the files
# category_data = []
# for category in categories:
#     category_data.append({
#         "name": category.name,
#         "img": category.imageUrl,
#         "description": category.description
#     })
# json.dump(category_data, category_file,indent=4)

place_data = []
for place in places:
    place_data.append({
        "title": place.name,
        "description": place.description,
        "price": place.price,
        "category": place.category.name,
        "image": place.imageUrl
    })


json.dump(place_data, place_file, indent=4)

# picture_data = []
# for picture in pictures:
#     picture_data.append({
#         "title": picture.place.name,
#         "images": [image.image_url for image in pictures if image.place == picture.place]
#     })

# json.dump(picture_data, picture_file)
#close the files
place_file.close()
# category_file.close()
# picture_file.close()
