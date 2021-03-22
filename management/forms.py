from django import forms
from .widgets import CustomClearableFileInput
from services.models import Services, Category
from portfolio.models import Portfolio, Portfolio_category


class ServiceForm(forms.ModelForm):
    """
    Form to create and edit services
    """
    class Meta:
        model = Services
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names


class PortfolioForm(forms.ModelForm):
    """
    Form to create and edit projects in the portfolio
    """
    class Meta:
        model = Portfolio
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Portfolio_category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
