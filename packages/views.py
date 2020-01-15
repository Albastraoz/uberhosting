from django.shortcuts import render
from .models import Package

# Create your views here.
def all_packages(request):
    packages = Package.objects.all()
    return render(request, "packages.html", {"packages": packages})