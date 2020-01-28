from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse

from . import views

# Create your tests here.
class PageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
    
    def test_aboutus_page_status_code(self):
        response = self.client.get('/aboutus/')
        self.assertEquals(response.status_code, 200)