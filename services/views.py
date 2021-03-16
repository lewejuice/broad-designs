from django.shortcuts import render
from contact.forms import ContactForm


def services(request):
    """ A view to navigate to the what we do page """

    contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'services/services.html', context)
