from django.shortcuts import render
from .models import Portfolio


def all_design(request):
    """ A view to navigate to the design page and display portfolio of design work"""
    projects = Portfolio.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'portfolio/design.html', context)


def all_code(request):
    """ A view to navigate to the code page """
    projects = Portfolio.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'portfolio/code.html', context)

