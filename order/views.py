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
    }

    return render(request, template, context)