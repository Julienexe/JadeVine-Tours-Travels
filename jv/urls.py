from django.urls import path
from . import views

app_name = 'jv'

urlpatterns = [
    # Add your URL patterns here
    path('', views.home, name='home'),
    path("popular_places/",views.popular_places,name='popular_places'),
    path("services/",views.services,name='services'),
    path("contact/",views.contact,name='contact'),
    path("about/",views.about,name='about'),
    path("gallery/",views.gallery,name='gallery'),
]