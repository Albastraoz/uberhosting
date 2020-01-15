from django.conf.urls import url, include
from .views import all_packages

urlpatterns = [
    url(r'^$', all_packages, name='packages')
]