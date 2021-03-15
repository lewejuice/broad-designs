from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order
from services.models import Services
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from bagged_services.contexts import order_contents

import stripe


@require_POST
def cache_order_data(request):
    if request.POST.get('useful_links') == '':
        useful_links = 'None'
    else:
        useful_links = request.POST.get('useful_links')
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'service_order': get_order_services(request),
            'save_info': request.POST.get('save_info'),
            'project_name': request.POST.get('project_name'),
            'target_audience': request.POST.get('target_audience'),
            'project_description': request.POST.get('project_description'),
            'useful_links': useful_links,
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def get_order_services(request):
    """
    Get the names of services in the order
    """
    current_bagged_services = order_contents(request)
    order = current_bagged_services['order_items']
    order_list = []
    if order:
        for item in order[0:2:1]:
            order_list.append(item['service'].name)
    service_order = ', '.join(order_list)

    return service_order


def get_order_total(request):
    """
    Get the order total
    """
    order = order_contents(request)
    total = order['order_total']

    return total


@login_required
def order(request):
    """
    Form to process the order
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    total = get_order_total(request)
    service_order = get_order_services(request)

    if request.method == 'POST':
        order = request.session.get('order', {})
        order_form = OrderForm(request.POST, request.FILES)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
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

    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.default_full_name,
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                'country': profile.default_country,
                'postcode': profile.default_postcode,
                'town_or_city': profile.default_town_or_city,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'county': profile.default_county,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
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

    profile = UserProfile.objects.get(user=request.user)
    # Attach the user's profile to the order
    order.user_profile = profile
    order.save()

    # Save the user's info
    if save_info:
        profile_data = {
            'default_phone_number': order.phone_number,
            'default_country': order.country,
            'default_postcode': order.postcode,
            'default_town_or_city': order.town_or_city,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_county': order.county,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'order_contents' in request.session:
        del request.session['order_contents']

    template = 'order/order_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
