from django.shortcuts import render
from .models import *

def home(request):
    return render(request,"jv/index.html")
def gallery(request):
    return render(request,"jv/gallery.htm")
def about(request):
    return render(request,"jv/about.htm")
def contact(request):
    return render(request,"jv/contact.htm")
def services(request):
    return render(request,"jv/services.htm")
def popular_places(request):
    places = Place.objects.all()
    print(places)
    context = {'places':places}
    return render(request,"jv/popular_places.htm",context)

