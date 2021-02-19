from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_number', 'project_name', 'target_audience', 'project_description',
                  'img_file', 'useful_links', 'username', 'order_paid',
                  'price', 'order_date', 'project_services')
