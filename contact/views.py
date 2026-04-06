from django.shortcuts import render

# Create your views here.

from .models import ContactMessage

def contact(request):

    if request.method == "POST":

        ContactMessage.objects.create(

            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']

        )

        return render(request, "contact.html", {"success": True})

    return render(request, "contact.html")