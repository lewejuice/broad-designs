from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Services
from django.utils import timezone, dateformat


def order_contents(request):

    order_items = []
    total = 0
    order = request.session.get('order', {})
    current_date = dateformat.format(timezone.now(), 'Y-m-d')

    for service_id in order.items():
        service = get_object_or_404(Services, pk=service_id[0])
        total += service.price
        order_items.append({
            'service_id': service_id[0],
            'service': service,
        })

    context = {
        'order_items': order_items,
        'total': total,
        'current_date': current_date
    }

    return context
