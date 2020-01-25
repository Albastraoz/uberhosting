from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=40, blank=False)
    message = models.TextField(max_length=500, blank=False)