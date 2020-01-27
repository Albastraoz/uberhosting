from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Model for extra profile information which is linked to User model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    street_address1 = models.CharField(max_length=40, blank=True)
    street_address2 = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=True)

# If new user is registered this will create Profile model and link to User model
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Saves the Profile model
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()