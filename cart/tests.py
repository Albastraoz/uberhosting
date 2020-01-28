from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse

from . import views

# Create your tests here.
class PostTests(TestCase):
    def test_cart_page_status_code(self):
        response = self.client.get('/cart/')
        self.assertEquals(response.status_code, 200)