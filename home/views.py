from django.shortcuts import render
from contact.forms import ContactForm

# Create your views here.


def index(request):
    """ A view to return the index page """

    contact_form = ContactForm()
    context = {
        'contact_form': contact_form
    }

    return render(request, 'home/index.html', context)


def google(request):
    """ A view to return the index page """

    contact_form = ContactForm()
    context = {
        'contact_form': contact_form
    }

    return render(request, 'home/google3e1e27baf2f49bd0.html.html', context)
