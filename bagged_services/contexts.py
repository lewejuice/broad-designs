import uuid
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Services
from contact.forms import ContactForm


def order_contents(request):

    order_items = []
    order_total = 0
    order = request.session.get('order', {})
    contact_form = ContactForm()

    for service_id in order.items():
        service = get_object_or_404(Services, pk=service_id[0])
        order_total += service.price
        order_items.append({
            'service_id': service_id[0],
            'service': service,
        })

    order_tile = order_items[0:2:1]
    order_object = order_tile[0]

    context = {
        'order_items': order_items,
        'order_total': order_total,
        'order_object': order_object,
        'contact_form': contact_form,
    }

    return context
