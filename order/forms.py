from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name_company', 'target_audience', 'project_description',
                  'img_file', 'useful_links',)
