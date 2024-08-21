from django.forms import ModelForm
from .models import Testimonial

class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'
        exclude= ['image']