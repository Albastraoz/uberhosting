from django.db import models
from packages.models import Package

# Order model to send to admin panel if order is successfull
class Order(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=True)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.first_name, self.last_name)

# Admin model for orders
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    package = models.ForeignKey(Package, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.package.name, self.package.price)