from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.utils import timezone

from services.models import Services
from .forms import OrderForm
from .models import Order

# Create your views here.


def order(request):
    """ A view to navigate to the what we do page and manage order form """

    services = Services.objects.all()
    design_services = Services.objects.filter(category='1')
    code_services = Services.objects.filter(category='2')

    context = {
        'services': services,
        'design_services': design_services,
        'code_services': code_services,
    }

    return render(request, 'order/order.html', context)


def add_to_order(request, service_id):
    """ Add services to users order """

    service = get_object_or_404(Services, pk=service_id[0])
    order = request.session.get('order', {})

    if service_id in list(order.keys()):
        remove_from_order(request, service_id, order)
    else:
        order[service_id] = 1
        messages.success(request, f'Added {service.name} to your order')

    request.session['order'] = order

    return redirect(reverse("order"))


def remove_from_order(request, service_id, order):
    """Remove item from the order"""

    service = get_object_or_404(Services, pk=service_id[0])

    try:
        order.pop(service_id)
        messages.success(request, f'Removed {service.name} from your order')

        request.session['order'] = order
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)


def project_form(request):
    """ A form to get the project details from the user """
    order_form = OrderForm()
    print(order_form)
    if request.method == 'POST':
        order_form = OrderForm(request.POST, request.FILES)
        if order_form.is_valid():
            order_form.save()
            messages.success(request, f'Your project has been created')
        else:
            messages.error(request, 'Form was invalid')
            print(order_form)

    context = {
        'order_form': order_form,
    }

    return render(request, 'payment/payment.html', context)
