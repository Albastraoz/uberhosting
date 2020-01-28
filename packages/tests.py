from django.test import TestCase
from .models import Package

# Create your tests here.
class PackageTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Package model
    """

    def test_str(self):
        test_name = Package(name='A product')
        self.assertEqual(str(test_name), 'A product')