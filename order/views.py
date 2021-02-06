from django.shortcuts import render, redirect
from services.models import Services
from django.urls import reverse

# Create your views here.


def order(request):
    """ A view to navigate to the what we do page """

    services = Services.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'order/order.html', context)


def add_to_order(request, service_id):
    """ Add or remove services on users order """

    order = request.session.get('order', {})

    if service_id in list(order.keys()):
        # remove_from_order()
        print("remove from order")
    else:
        order[service_id] = 1

    request.session['order'] = order

    return redirect(reverse("order"))
