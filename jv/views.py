from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import TestimonialForm
from .models import *

def home(request):
    categories = Category.objects.all().exclude(name='Stone Town City Tour')
    places = Place.objects.all()[:9]
    context = {
        'categories': categories,
        'places': places
    }
    return render(request,"jv/index.html",context)


@csrf_exempt  # Use this decorator if you haven't included the CSRF token in the AJAX request
def create_testimonial(request):
    if request.method == 'POST':

        
        name = request.POST.get("yrNames")
        country = request.POST.get('yourCountry')
        title = request.POST.get('title')
        gender = request.POST.get('gender')
        test = request.POST.get('description')
        
        try:
            Testimonial.objects.create(
                name = name,
                country = country,
                title = title,
                gender = gender,
                testimonial = test,
                image = request.FILES
            )
           
            response_data = {
                'status': 1,
                'message': 'Testimonial submitted successfully!',
            }
        except:
            
            response_data = {
                'status': 0,
                'message': 'There was an error with your submission. Please check the form and try again.',
            }
        return JsonResponse(response_data)
    else:
        # If the request is not a POST request, return a bad request response
        return JsonResponse({'status': 0, 'message': 'Invalid request method.'})


