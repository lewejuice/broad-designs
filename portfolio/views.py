from django.shortcuts import render
from .models import Portfolio

# Create your views here.


def design(request):
    """ A view to navigate to the design page """
    projects = Portfolio.objects.all()

    context = {
        'Portfolio': projects,
    }

    return render(request, 'portfolio/design.html', context)


def code(request):
    """ A view to navigate to the code page """

    return render(request, 'portfolio/code.html')