from django.test import TestCase, Client


# Create your tests here.
class TestCaseMain(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_privacy(self):
        response = self.client.get('/privacy/')
        self.assertEqual(response.status_code, 200)

    def test_terms(self):
        response = self.client.get('/terms/')
        self.assertEqual(response.status_code, 200)