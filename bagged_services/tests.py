from django.test import TestCase
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from services.models import Services


class TestViews(TestCase):
    """
    Testing the Views
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username="TestUser", password="Passw0rd")
        self.client.login(username="TestUser", password="Passw0rd")
        Services.objects.create(
            name="Test Service",
            price=10.00).save()

    def test_get_bagged_services(self):
        response = self.client.get('/bagged_services/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'bagged_services/bagged_services.html')

    def test_can_add_to_order(self):
        order = self.client.session
        service = Services.objects.get(name="Test Service")
        response = self.client.post(f'/bagged_services/add/{service}')
        self.assertRedirects(response, '/')


    # def test_can_remove_from_order(self):
