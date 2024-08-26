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
    path('createTestimonial/', views.create_testimonial, name='createTestimonial'),
    path('createInquiry/', views.create_inquiry, name='inquiry'),
    path("contact",views.contact_us,name="contact"),
    path("category/<int:category_id>",views.category,name="category"),
    path("place/<int:place_id>",views.place,name="place"),
    path('search/', views.search_cat,name='search'),
    path('search-place/',views.search_place,name='search-place')
    
]