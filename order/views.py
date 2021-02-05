from django.shortcuts import render, redirect
from services.models import Services

# Create your views here.


def order(request):
    """ A view to navigate to the what we do page """

    services = Services.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'order/order.html', context)


def add_to_order(request, service_id):
    """ Add or remove services on users order """

    redirect_url = request.POST.get('redirect_url')
    order = request.session.get('order', {})

    if service_id in list(order.keys()):
        remove_from_order()
    else:
        order[service_id]

    request.session['order'] = order
    print(request.session['order'])
    return redirect(redirect_url)
