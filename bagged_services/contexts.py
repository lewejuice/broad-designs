from django.shortcuts import get_object_or_404
from services.models import Services
from contact.forms import ContactForm


def order_contents(request):
    """
    A context to enable the contact for to render on each page,
    and too hold the order info.
    """
    order_items = []
    order_total = 0
    order = request.session.get('order', {})
    contact_form = ContactForm()
    order_objects = []

    for service_id in order.items():
        service = get_object_or_404(Services, pk=service_id[0])
        order_total += service.price
        order_items.append({
            'service_id': service_id[0],
            'service': service,
        })
        added_service_id = int(service_id[0])
        order_objects.append(added_service_id)

    context = {
        'order_items': order_items,
        'order_total': order_total,
        'order_objects': order_objects,
        'contact_form': contact_form,
    }

    return context
