from django.shortcuts import render

# Create your views here.

from .models import Home

def home(request):

    data = Home.objects.first()

    return render(request, "home.html", {"data": data})