from decimal import Decimal
from django.conf import settings

def order_contents(request):

    order_items = []
    total = 0
    service_count = 0

    context = {
        'order_items': order_items,
        'total': total,
        'service_count': service_count,
    }

    return context
