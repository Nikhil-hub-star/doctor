from django.test import TestCase

# Create your tests here.
class ContactTest(TestCase):

    def test_contact_page(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)