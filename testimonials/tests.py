from django.test import TestCase

# Create your tests here.
class TestimonialTest(TestCase):

    def test_testimonial_page(self):
        response = self.client.get('/testimonials/')
        self.assertEqual(response.status_code, 200)