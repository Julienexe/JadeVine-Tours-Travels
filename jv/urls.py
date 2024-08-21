from django.urls import path
from . import views

app_name = 'jv'

urlpatterns = [
    # Add your URL patterns here
    path('', views.home, name='home'),
    path('createTestimonial/', views.create_testimonial, name='createTestimonial'),
]