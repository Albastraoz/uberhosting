from django.shortcuts import render
from packages.models import Package

def index(request):
    # A view that displays the homepage
    packages = Package.objects.all()
    return render(request, "index.html", {"packages": packages})

def aboutus(request):
    # A view that displays the about us page
    return render(request, "aboutus.html")