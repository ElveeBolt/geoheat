from django.test import TestCase, Client


# Create your tests here.
class TestCaseHelp(TestCase):
    def setUp(self):
        self.client = Client()

    def test_open_page(self):
        response = self.client.get('/help/')
        self.assertEqual(response.status_code, 200)