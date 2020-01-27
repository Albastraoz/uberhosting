from django.shortcuts import render
from .models import Package

# Gets all packages from DB
def all_packages(request):
    packages = Package.objects.all()
    return render(request, "packages_base.html", {"packages": packages})