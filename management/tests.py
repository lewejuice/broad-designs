from django.test import TestCase
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from services.models import Services, Category
from portfolio.models import Portfolio, Portfolio_category
from order.models import Order
from .forms import ServiceForm, PortfolioForm


# ----- FORMS -----

class TestServiceForm(TestCase):
    """
    Testing the Service Form
    """
    def test_can_create_and_edit_services(self):
        form = ServiceForm(
            {'name': 'Test Service',
                'price': '100.00'})
        self.assertTrue(form.is_valid())

    def test_service_name_is_required(self):
        form = ServiceForm(
            {'name': '',
                'price': '100.00'})
        self.assertFalse(form.is_valid())


class TestPortfolioForm(TestCase):
    """
    Testing the Portfolio Form
    """
    def test_can_create_and_edit_projects_in_portfolio(self):
        form = PortfolioForm(
            {'name': 'Test Service',
                'project_date': '2020-09-20',
                'description': 'Testing',
                'image': 'test.jpg'})
        self.assertTrue(form.is_valid())

    def test_projects_date_format_is_correct(self):
        form = PortfolioForm(
            {'name': 'Test Service',
                'project_date': '19th January 2020',
                'description': 'Testing',
                'image': 'test.jpg'})
        self.assertFalse(form.is_valid())


# ----- VIEWS -----

class TestViews(TestCase):
    """
    Testing the Views
    """
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='TestUser', password='Passw0rd')
        self.client.login(username='TestUser', password="Passw0rd")
        Category.objects.create(name='Test Category').save()
        Services.objects.create(name='Test Service', price=10.00).save()
        Portfolio_category.objects.create(name='Test Category').save()
        Portfolio.objects.create(name='Test Service',
                                 project_date='2020-09-20',
                                 description='Testing',
                                 image='test.jpg').save()
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

    def test_get_management(self):
        response = self.client.get('/management/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'management/management.html')

    def test_get_edit_service(self):
        service = Services.objects.get(name='Test Service', price=10.00)

        response = self.client.get(f'/management/edit-service/{service.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'management/edit_service.html')

        response2 = self.client.post(f'/management/edit-service/{service.id}/')
        self.assertEqual(response2.status_code, 200)

    def test_can_add_service(self):
        response = self.client.get('/management/add-service/')
        self.assertEqual(response.status_code, 200)

    def test_get_delete_service_page(self):
        service = Services.objects.get(name='Test Service')
        response = self.client.get(
            f'/management/delete-service-page/{service.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'management/delete_service.html')

    def test_can_delete_service(self):
        service = Services.objects.get(name="Test Service")
        response = self.client.post(
            f'/management/delete-service/{service.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/management/')

    def test_can_add_project(self):
        response = self.client.get('/management/add-project/')
        self.assertEqual(response.status_code, 200)

    def test_get_edit_project(self):
        project = Services.objects.get(name='Test Service')
        response = self.client.get(f'/management/edit-project/{project.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'management/edit_project.html')

    def test_get_delete_project_page(self):
        project = Services.objects.get(name='Test Service')
        response = self.client.get(
            f'/management/delete-project-page/{project.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'management/delete_project.html')

    def test_can_delete_project(self):
        project = Services.objects.get(name='Test Service')
        response = self.client.post(
            f'/management/delete-project/{project.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/management/')

    def test_get_order_info_page(self):
        order = Order.objects.get(order_number='12345')
        response = self.client.get(
            f'/management/order-info/{order.order_number}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'management/order_info.html')
