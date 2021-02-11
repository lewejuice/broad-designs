from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404

from services.models import Services
from .forms import OrderForm
from .models import Order

# Create your views here.


def order(request):
    """ A view to navigate to the what we do page """

    services = Services.objects.all()

    context = {
        'services': services,
    }

    if request.method == 'POST':
        form_data = {
            'name_company': request.POST['name_company'],
            'project_description': request.POST['project_description'],
            'target_audience': request.POST['target_audience'],
            'useful_links': request.POST['useful_links'],
            'img_file': request.POST['image_url'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order_form.save(commit=False)

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
