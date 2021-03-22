from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse


def contact(request):
    """
    A view to render a contact form, so users can ask questions via email
    """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            body = {
                'first_name': contact_form.cleaned_data['first_name'],
                'last_name': contact_form.cleaned_data['last_name'],
                'email_address': contact_form.cleaned_data['email_address'],
                'phone_number': contact_form.cleaned_data['phone_number'],
                'message': contact_form.cleaned_data['message'],
            }
            message = '\n'.join(body.values())
            cust_email = contact_form['email_address'].value()
            subject = 'Inquiry from: ' + cust_email
            receiving_email = settings.DEFAULT_FROM_EMAIL

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [receiving_email]
            )
            messages.success(request, 'Your message has been sent, \
                we will get back to you as soon as possible!')
            return redirect("home")
    messages.error(request, 'We are very sorry, \
                there seems to be a problem!')
    return render(request, "contact/contact.html")
