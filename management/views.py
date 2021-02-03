from django.shortcuts import render

# Create your views here.


def management(request):
    """ A view to navigate to the what we do page """

    return render(request, 'management/management.html')