from django.test import TestCase
from .forms import ContactForm


# ----- FORMS -----

class TestContactForm(TestCase):
    """
    Testing the Service Form
    """
    def test_can_send_contact_form(self):
        form = ContactForm(
            {'first_name': 'Test Name',
                'last_name': 'Test Name',
                'email_address': 'test@test.com',
                'phone_number': '077777777777',
                'message': 'Testing'})
        self.assertTrue(form.is_valid())

    def test_correct_error_message(self):
        form = ContactForm(
            {'first_name': 'Test Name',
                'last_name': 'Test Name',
                'email_address': '',
                'phone_number': '077777777777',
                'message': 'Test message'})
        self.assertEqual(
            form.errors["email_address"], [u"This field is required."])

    def test_message_is_required(self):
        form = ContactForm(
            {'first_name': 'Test Name',
                'last_name': 'Test Name',
                'email_address': 'test@test.com',
                'phone_number': '077777777777',
                'message': ''})
        self.assertFalse(form.is_valid())


# ----- VIEWS -----

class TestViews(TestCase):
    """
    Testing the Views
    """
    def test_get_contact_page(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'contact/contact.html')
