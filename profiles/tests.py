from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserProfileForm


# ----- FORMS -----

class TestUserProfileForm(TestCase):
    """
    Testing the Profile Form
    """
    def test_can_save_user_details(self):
        form = UserProfileForm(
            {'default_full_name': 'Test Name',
                'default_phone_number': '077777777777',
                'default_postcode': 'test',
                'default_town_or_city': 'Test',
                'default_street_address1': 'Test',
                'default_street_address2': 'Test',
                'default_county': 'gb'})
        self.assertTrue(form.is_valid())

    def test_can_user_phone_number_not_required(self):
        form = UserProfileForm(
            {'default_full_name': 'Test Name',
                'default_phone_number': '',
                'default_postcode': 'test',
                'default_town_or_city': 'Test',
                'default_street_address1': 'Test',
                'default_street_address2': 'Test',
                'default_county': 'gb'})
        self.assertTrue(form.is_valid())


# ----- VIEWS -----

class TestViews(TestCase):
    """
    Testing the Views
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='TestUser', password='Passw0rd')
        self.client.login(username='TestUser', password="Passw0rd")

    def test_get_profile(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'profiles/profile.html')
