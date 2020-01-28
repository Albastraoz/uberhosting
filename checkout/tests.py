from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse
from .models import Order
from django.utils import timezone

from . import views

# Create your tests here.
class CheckoutTests(TestCase):
    def setUp(self):
        self.order = Order()
        self.order.first_name = "Peter"
        self.order.last_name = "Coster"
        self.order.country = "England"
        self.order.postcode = "2356"
        self.order.town_or_city = "London"
        self.order.street_address1 = "Gandalfstreet 12"
        self.order.street_address2 = ""
        self.order.county = ""
        self.order.date = timezone.now()
        self.order.save()

    def test_checkout_fields(self):
        getorder = Order.objects.get(pk=self.order.id)
        self.assertEqual(getorder, self.order)

    def test_checkout_page_status_code(self):
        response = self.client.get('/checkout/')
        self.assertEquals(response.status_code, 302)