from django.test import TestCase


# ----- VIEWS -----

class TestViews(TestCase):
    """
    Testing the Views
    """
    def test_get_services(self):
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'services/services.html')
