from django.shortcuts import render

# Create your views here.


def services(request):
    """ A view to navigate to the what we do page """

    return render(request, 'services/services.html')
