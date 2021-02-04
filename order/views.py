from django.shortcuts import render
from services.models import Services

# Create your views here.


def order(request):
    """ A view to navigate to the what we do page """

    return render(request, 'order/order.html')
