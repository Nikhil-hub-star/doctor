from django.shortcuts import render

# Create your views here.

from .models import Testimonial

def testimonials(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')
    return render(request, "testimonials.html", {"testimonials": testimonials})