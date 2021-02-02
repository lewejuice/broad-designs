from django.shortcuts import render

# Create your views here.


def quotation(request):
    """ A view to navigate to the what we do page """

    return render(request, 'quotation/quote.html')
