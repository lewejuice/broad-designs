from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bagged_services.contexts import order_contents

import stripe


def order(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    order = request.session.get('order', {})
    if not order:
        messages.error(request, "There's nothing in your order at the moment")
        return redirect(reverse('bagged_services'))

    current_bagged_services = order_contents(request)
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
