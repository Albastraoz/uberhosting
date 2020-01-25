from django.shortcuts import render
from packages.models import Package
#from django.core.mail import send_mail

# Create your views here.

def index(request):
    # A view that displays the homepage
    packages = Package.objects.all()
    return render(request, "index.html", {"packages": packages})
