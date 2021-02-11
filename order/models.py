from django.db import models


class Order(models.Model):
    name_company = models.CharField(max_length=50, null=False, blank=False)
    project_description = models.CharField(max_length=99999, null=True, blank=True)
    target_audience = models.CharField(max_length=10, null=True, blank=True)
    useful_links = models.CharField(max_length=99999, null=True, blank=True)
    img_file = models.ImageField(upload_to='images/', null=True, blank=False)

    def __str__(self):
        return self.order_form
