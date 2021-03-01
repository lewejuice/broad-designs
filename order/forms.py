from django import forms
from django.forms import ModelForm, Textarea
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('project_name', 'target_audience',
                  'project_description', 'img_file',
                  'useful_links', 'full_name',
                  'email', 'phone_number', 'country',
                  'postcode', 'town_or_city', 'street_address1',
                  'street_address2', 'county')
        widgets = {
            'project_description': Textarea(attrs={'cols': 80, 'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'project_name': 'Project Name',
            'target_audience': 'Target Audience',
            'project_description': 'Project Description',
            'img_file': 'Upload a useful file',
            'useful_links': 'Useful Links',
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        self.fields['project_name'].widget.attrs['autofocus'] = True
        self.fields['project_description'].required = True
        self.fields['target_audience'].required = True
        self.fields['img_file'].required = False
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
