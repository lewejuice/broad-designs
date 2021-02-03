from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Services(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    service_id = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
