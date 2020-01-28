from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse
from .models import Package

from . import views

# Create your tests here.
class PackageTests(TestCase):
    def test_package_fields(self):
        item = Package()
        item.name = "Package name"
        item.price = 20.00
        item.domain = 20
        item.mail_space = 20000
        item.hosting_space = 40
        item.hosting_databases = 5
        item.apps = False
        item.highlight = False
        item.sftp = 4
        item.save()

        package = Package.objects.get(pk=item.id)
        self.assertEqual(package, item)

    def test_packages_page_status_code(self):
        response = self.client.get('/packages/')
        self.assertEquals(response.status_code, 200)