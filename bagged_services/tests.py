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

    def test_get_bagged_services(self):
        response = self.client.get('/bagged_services/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'bagged_services/bagged_services.html')

    def test_can_add_to_order(self):
        service = get_object_or_404(Services, pk=service_id[0])
        response = self.client.post(f'/add/{service.service_id}',
                                    {'service_id': 50})
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/')


    # def test_can_remove_from_order(self):
