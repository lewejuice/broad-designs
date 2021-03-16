from django.shortcuts import render
from .models import Portfolio
from contact.forms import ContactForm


def all_design(request):
    """ A view to navigate to the design page and display portfolio of design work"""
    projects = Portfolio.objects.all()
    contact_form = ContactForm()

    context = {
        'projects': projects,
        'contact_form': contact_form,
    }

    return render(request, 'portfolio/design.html', context)


def all_code(request):
    """ A view to navigate to the code page """
    projects = Portfolio.objects.all()
    contact_form = ContactForm()

    context = {
        'projects': projects,
        'contact_form': contact_form,
    }

    return render(request, 'portfolio/code.html', context)

