from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import ServiceForm
from services.models import Services
# Create your views here.


def management(request):
    """ A view to navigate to the what we do page """

    services = Services.objects.all()
    design_services = Services.objects.filter(category='1')
    code_services = Services.objects.filter(category='2')

    context = {
        'services': services,
        'design_services': design_services,
        'code_services': code_services,
    }

    return render(request, 'management/management.html', context)


def add_service(request):
    """ Add a new service """
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added service!')
            return redirect(reverse('add_service'))
        else:
            messages.error(request, 'Failed to add service. Please ensure the form is valid.')
    else:
        form = ServiceForm()
    template = 'management/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_service(request, service_id):
    """ Edit a service """
    service = get_object_or_404(Services, pk=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated service!')
            return redirect(reverse('edit_service'))
        else:
            messages.error(request, 'Failed to update service. Please ensure the form is valid.')
    else:
        form = ServiceForm(instance=service)
        messages.info(request, f'You are editing {service.name}')

    template = 'management/edit_service.html'
    context = {
        'form': form,
        'service': service,
    }

    return render(request, template, context)


def delete_service(request, service_id):
    """ Delete a product from the store """
    service = get_object_or_404(Services, pk=service_id)
    service.delete()
    messages.success(request, 'Service deleted!')

    return render(request, 'management/management.html')
