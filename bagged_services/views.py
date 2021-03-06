from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from services.models import Services


@login_required
def bagged_services(request):
    """
    A view to navigate to the bagged services page,
    so users can add or delete items in their order.
    """

    services = Services.objects.all()
    design_services = Services.objects.filter(category='1')
    code_services = Services.objects.filter(category='2')

    context = {
        'services': services,
        'design_services': design_services,
        'code_services': code_services,
    }

    return render(request, 'bagged_services/bagged_services.html', context)


@login_required
def add_to_order(request, service_id):
    """ Add services to users order """

    service = get_object_or_404(Services, pk=service_id[0])
    order = request.session.get('order', {})

    if service_id in list(order.keys()):
        remove_from_order(request, service_id, order)
    elif service_id not in list(order.keys()):
        order[service_id] = 1
        messages.success(request, f'Added {service.name} to your order')
    else:
        messages.error(request, 'Oops something went wrong')
        return render(request, 'bagged_services.html')

    request.session['order'] = order

    return redirect(reverse("bagged_services"))


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
