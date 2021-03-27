from django.test import TestCase
from django.contrib.auth.models import User
from .models import Portfolio, Portfolio_category


# ----- VIEWS -----

class TestViews(TestCase):
    """
    Testing the Views
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='TestUser', password='Passw0rd')
        self.client.login(username='TestUser', password="Passw0rd")
        Portfolio_category.objects.create(name='Test Category').save()
        Portfolio.objects.create(name='Test Service',
                                 project_date='2020-09-20',
                                 description='Testing',
                                 image='test.jpg').save()

    def test_get_design_portfolio(self):
        response = self.client.get('/portfolio/design/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'portfolio/design.html')

    def test_get_code_portfolio(self):
        response = self.client.get('/portfolio/code/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'portfolio/code.html')
