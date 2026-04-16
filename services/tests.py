from django.test import TestCase

# Create your tests here.
class ServiceTest(TestCase):

    def test_services_page(self):
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)