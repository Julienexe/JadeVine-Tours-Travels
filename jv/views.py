from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File as DjangoFile
from django.shortcuts import render

#from .forms import TestimonialForm
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
    categories = Category.objects.all()
    return render(request,"jv/services.htm",{"categories":categories})
def popular_places(request):
    places = Place.objects.all()
    
    return render(request, 'jv/popular_places.htm', {'places': places})

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    places = Place.objects.filter(category=category)
    return render(request, 'jv/popular_places.htm', {'category': category, 'places': places})


def home(request):
    categories = Category.objects.all().exclude(name='Stone Town City Tour')
    places = Place.objects.all()[:9]
    testimonials = Testimonial.objects.all()
    context = {
        'categories': categories,
        'places': places,
        'testimonials': testimonials
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
        img = DjangoFile(request.FILES['photo'], name=request.FILES['photo'].name)    
        
        try:
            test = Testimonial.objects.create(
                name = name,
                country = country,
                title = title,
                gender = gender,
                testimonial = test,
                image = img
            )
           
            response_data = {
                'status': 1,
                'message': 'Testimonial submitted successfully!',
                "name": test.name,
                'country': test.country,
                'title': test.title,
                'testimonial': test.testimonial,
                'photo': test.image.url
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

def create_inquiry(request):
    if request.method =="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        type = request.POST.get("type")
        other = request.POST.get("other")
        departure_date = request.POST.get("departure_date")
        return_date = request.POST.get("return_date")
        destination = request.POST.get("destination")
        no_of_adults = request.POST.get("adults")
        no_of_children = request.POST.get("children")

       
        inquiry = Inquiry.objects.create(
            name = name,
            email = email,
            type = type,
            other = other if other else None,
            departure_date = departure_date,
            return_date = return_date,
            destination = destination,
            no_of_adults = no_of_adults,
            no_of_children = no_of_children
        )
    
        
    return home(request)

@csrf_exempt
def contact_us(request):
    #to be populated later
    response_data = {
                'status': 1,
                'message': 'Message submitted successfully!',
            }
    return JsonResponse(response_data)
    

