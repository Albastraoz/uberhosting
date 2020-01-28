from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse
from .models import Contact

from . import views

# Create your tests here.
class ContactTests(TestCase):
    def setUp(self):
        self.question = Contact()
        self.question.full_name = "Peter Coster"
        self.question.email = "person@email.com"
        self.question.message = "This is just a random message as an example"
        self.question.save()

    def test_checkout_fields(self):
        sendmessage = Contact.objects.get(pk=self.question.id)
        self.assertEqual(sendmessage, self.question)

    def test_checkout_page_status_code(self):
        response = self.client.get('/contact/')
        self.assertEquals(response.status_code, 200)