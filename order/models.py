import uuid

from django.db import models
from django.conf import settings


class Order(models.Model):

    class Meta:
        verbose_name_plural = 'Orders'

    project_name = models.CharField(max_length=50, null=False, blank=False)
    target_audience = models.CharField(max_length=10, null=True, blank=True)
    project_description = models.CharField(max_length=99999, null=True, blank=True)
    img_file = models.ImageField(upload_to='media/', null=True, blank=False)
    useful_links = models.CharField(max_length=99999, null=True, blank=True)
    username = models.CharField(max_length=50, null=False, blank=False)
    project_services = models.CharField(max_length=10000, null=True, blank=True)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
