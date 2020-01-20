from django.shortcuts import render
from packages.models import Package

# Create your views here.

def index(request):
    # A view that displays the homepage
    packages = Package.objects.all()
    return render(request, "index.html", {"packages": packages})