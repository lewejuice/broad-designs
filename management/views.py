from django.shortcuts import render
from .forms import ServiceForm

# Create your views here.


def management(request):
    """ A view to navigate to the what we do page """

    return render(request, 'management/management.html')


def add_service(request):
    """ Add a product to the store """
    form = ServiceForm()
    template = 'management/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
