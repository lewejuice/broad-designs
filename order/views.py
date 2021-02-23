from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order
from services.models import Services
from bagged_services.contexts import order_contents

import stripe


def order(request):
    """
    Form to process the order
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    current_bagged_services = order_contents(request)
    order = current_bagged_services['order_items']
    total = current_bagged_services['order_total']
    order_list = []
    if order:
        for item in order[0:2:1]:
            order_list.append(item['service'].name)
    service_order = ', '.join(order_list)

    if request.method == 'POST':
        order = request.session.get('order', {})
        order_form = OrderForm(request.POST, request.FILES)
        if order_form.is_valid():
            order = order_form.save()
            order.username = request.user.username
            order.project_services = service_order
            order.order_total = total
            order.save()
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('order_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        order = request.session.get('order', {})
        if not order:
            messages.error(request, "There's nothing in your order at the moment")
            return redirect(reverse('bagged_services'))

    total = current_bagged_services['order_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'order/order.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def order_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'order_items' in request.session:
        del request.session['order_items']

    template = 'order/order_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
