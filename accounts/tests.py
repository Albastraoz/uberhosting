from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile

from . import views

# Create your tests here.
class ProfileTests(TestCase):
    def setUp(self):
        self.user = User()
        self.user.username = "randomname"
        self.user.email = "random@email.com"
        self.user.password = "ThisisAPassword123"

        self.user.profile = Profile()
        self.user.profile.phone_number = 123456789
        self.user.profile.contry = "England"
        self.user.profile.postcode = "2356"
        self.user.profile.town_or_city = "London"
        self.user.profile.street_address1 = "Gandalfstreet 12"
        self.user.profile.street_address2 = ""
        self.user.profile.county = ""

        self.user.save()

    def test_user_creation(self):
        accountUser = User.objects.get(pk=self.user.id)
        self.assertEqual(accountUser, self.user)
    
    def test_profile_creation(self):
        accountProfile = User.objects.get(pk=self.user.id)
        self.assertEqual(accountProfile.profile, self.user.profile)

    def test_login_page_status_code(self):
        response = self.client.get('/accounts/login/')
        self.assertEquals(response.status_code, 200)
    
    def test_register_page_status_code(self):
        response = self.client.get('/accounts/register/')
        self.assertEquals(response.status_code, 200)

    def test_profile_page_status_code(self):
        response = self.client.get('/accounts/profile/')
        self.assertEquals(response.status_code, 302)