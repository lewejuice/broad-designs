from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def order(request):
    order = request.session.get('order', {})
    if not order:
        messages.error(request, "There's nothing in your order at the moment")
        return redirect(reverse('bagged_services'))

    order_form = OrderForm()
    template = 'order/order.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HxpOtKDGGKaeBiRhKPJ3n8zsWtDQAq1QHp3nz9gtnAO5xL6WlZAEaIG4vNaAV2UbpDQXG7Xoy051jyHQi4H0tFC00xJezbLH0',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
