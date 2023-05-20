from django.contrib.auth.models import User
from django.test import TestCase, Client
from location.models import Location, Marker


class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(username='admin', password='admin', email='admin@mail.com')

    def test_user_signup(self):
        response = self.client.post('/user/signup', {
            'username': 'testuser',
            'password': '030496',
            'email': 'test@mail.com',

        })

        try:
            user = User.objects.filter(username='testuser')
        except User.DoesNotExist:
            user = None

        self.assertIsNotNone(user)

    def test_user_signup_auth(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get('/user/signup/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/user/')

    def test_user_login_auth(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get('/user/login/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')