from django.test import TestCase

# Create your tests here.
class AppointmentTest(TestCase):

    def test_appointment_page(self):
        response = self.client.get('/appointment/')
        self.assertEqual(response.status_code, 200)