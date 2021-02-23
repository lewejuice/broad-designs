from django import forms
from .models import Order
from .widgets import CustomClearableFileInput


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('project_name', 'target_audience',
                  'project_description', 'img_file',
                  'useful_links', 'full_name',
                  'email', 'phone_number', 'country',
                  'postcode', 'town_or_city', 'street_address1',
                  'street_address2', 'county',
        )

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
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['project_name'].widget.attrs['autofocus'] = True
        self.img_file = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
