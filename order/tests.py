from django.test import TestCase
from django.contrib.auth.models import User
from .models import Order
from .forms import OrderForm


# ----- FORMS -----

class TestServiceForm(TestCase):
    """
    Testing the Service Form
    """
    def test_can_create_and_edit_services(self):
        form = OrderForm(
            {'project_name': 'Test name',
                'target_audience': 'Test',
                'project_description': 'Testing',
                'img_file': 'test.jpg',
                'useful_links': 'test',
                'full_name': 'test',
                'email': 'test@test.com',
                'phone_number': '0777777777',
                'country': 'gb',
                'postcode': 'CT11 7EG',
                'town_or_city': 'test',
                'street_address1': 'test',
                'street_address2': 'test',
                'county': 'test'})
        self.assertTrue(form.is_valid())

    def test_order_email_is_required(self):
        form = OrderForm(
            {'project_name': 'Test name',
                'target_audience': 'Test',
                'project_description': 'Testing',
                'img_file': 'test.jpg',
                'useful_links': 'test',
                'full_name': 'test',
                'email': '',
                'phone_number': '0777777777',
                'country': 'gb',
                'postcode': 'test',
                'town_or_city': 'test',
                'street_address1': 'test',
                'county': 'test'})
        self.assertFalse(form.is_valid())

    def test_order_img_file_is_not_required(self):
        form = OrderForm(
            {'project_name': 'Test name',
                'target_audience': 'Test',
                'project_description': 'Testing',
                'img_file': 'test.jpg',
                'useful_links': 'test',
                'full_name': 'test',
                'email': 'test@test.com',
                'phone_number': '0777777777',
                'country': 'gb',
                'postcode': 'test',
                'town_or_city': 'test',
                'street_address1': 'test',
                'county': 'test'})
        self.assertTrue(form.is_valid())


# ----- VIEWS -----

class TestViews(TestCase):
    """
    Testing the Views
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='TestUser', password='Passw0rd')
        Order.objects.create(project_name='Test name',
                             target_audience='Test',
                             project_description='Testing',
                             img_file='test.jpg',
                             useful_links='test',
                             username='test',
                             project_services='test',
                             order_number='12345',
                             full_name='test',
                             email='test@test.com',
                             phone_number='0777777777',
                             country='gb',
                             postcode='test',
                             town_or_city='test',
                             street_address1='test',
                             county='test',
                             date='2020-09-20',
                             order_total='100.00',
                             stripe_pid='000')

    def test_get_order(self):
        response = self.client.get('/order/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'order/order.html')
