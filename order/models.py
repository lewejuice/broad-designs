from django.db import models
from django.utils import timezone


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Order(models.Model):

    class Meta:
        verbose_name_plural = 'Orders'

    username = models.CharField(max_length=50, null=False, blank=False)
    project_name = models.CharField(max_length=50, null=False, blank=False)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    order_date = models.DateField(editable=False)
    order_paid = models.BooleanField(default=False)
    project_description = models.CharField(max_length=99999, null=True, blank=True)
    target_audience = models.CharField(max_length=10, null=True, blank=True)
    useful_links = models.CharField(max_length=99999, null=True, blank=True)
    img_file = models.ImageField(upload_to='media/', null=True, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.username:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.project_name
