from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import ServiceForm
from .forms import PortfolioForm
from services.models import Services
from portfolio.models import Portfolio
from order.models import Order
from profiles.models import UserProfile


def management(request):
    """ A view to navigate to the what we do page """

    services = Services.objects.all()
    design_services = Services.objects.filter(category='1')
    code_services = Services.objects.filter(category='2')
    portfolio = Services.objects.all()
    design_portfolio = Portfolio.objects.filter(category='2')
    code_portfolio = Portfolio.objects.filter(category='1')
    orders = Order.objects.all()
    profiles = UserProfile.objects.all()

    context = {
        'services': services,
        'design_services': design_services,
        'code_services': code_services,
        'portfolio': portfolio,
        'design_portfolio': design_portfolio,
        'code_portfolio': code_portfolio,
        'orders': orders,
        'profiles': profiles,
    }

    return render(request, 'management/management.html', context)


def add_service(request):
    """ Add a new service """
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added service!')
            return redirect('management')
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
            return redirect('management')
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


def delete_service_page(request, service_id):
    """ A view to navigate to the delete service page """
    service = get_object_or_404(Services, pk=service_id)
    template = 'management/delete_service.html'

    context = {
        'service': service,
    }

    return render(request, template, context)


def delete_service(request, service_id):
    """ Delete a service """
    service = get_object_or_404(Services, pk=service_id)
    service.delete()
    messages.success(request, 'Service deleted!')

    return redirect('management')


def add_project(request):
    """ Add a project to portfolio """
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added project to portfolio!')
            return redirect('management')
        else:
            messages.error(request, 'Failed to add project. Please ensure the form is valid.')
    else:
        form = PortfolioForm()

    template = 'management/add_project.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_project(request, project_id):
    """ Edit a service """
    project = get_object_or_404(Portfolio, pk=project_id)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated project!')
            return redirect('management')
        else:
            messages.error(request, 'Failed to update project. Please ensure the form is valid.')
    else:
        form = PortfolioForm(instance=project)
        messages.info(request, f'You are editing {project.name}')

    template = 'management/edit_project.html'
    context = {
        'form': form,
        'project': project,
    }

    return render(request, template, context)


def delete_project_page(request, project_id):
    """ A view to navigate to the delete project page """
    project = get_object_or_404(Portfolio, pk=project_id)
    template = 'management/delete_project.html'

    context = {
        'project': project,
    }

    return render(request, template, context)


def delete_project(request, project_id):
    """ Delete a project """
    project = get_object_or_404(Portfolio, pk=project_id)
    project.delete()
    messages.success(request, 'Project deleted!')

    return redirect('management')


def order_info(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    template = 'management/order_info.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
