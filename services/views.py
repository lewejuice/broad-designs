from django.shortcuts import render


def services(request):
    """ A view to navigate to the what we do page """

    return render(request, 'services/services.html')
