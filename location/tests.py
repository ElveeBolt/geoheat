from django.contrib.auth.models import User
from django.test import TestCase, Client
from location.models import Location, Marker


# Create your tests here.
class LocationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(username='admin', password='admin')
        Location.objects.create(user=user, title='Локация 1', description='Описание локации', lat=15.50689, lng=32.69887)
        Location.objects.create(user=user, title='Локация 2', description='Описание локации', lat=15.50689, lng=32.69887)

    def test_location_post(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post('locations/create', {
            'title': 'Локация 3',
            'description': 'Описание локации',
            'lat': 15.50689,
            'lng': 32.69887
        })

        try:
            location = Location.objects.filter(title='Локация 3')
        except Location.DoesNotExist:
            location = None

        self.assertIsNotNone(location)

    def test_location_delete(self):
        self.client.login(username='admin', password='admin')
        location = Location.objects.get(title='Локация 1')
        response = self.client.post(f'/locations/{location.id}/delete')

        try:
            location = Location.objects.filter(id=location.id)
        except Location.DoesNotExist:
            location = None

        self.assertIsNotNone(location)

    def test_location_update(self):
        self.client.login(username='admin', password='admin')
        location = Location.objects.get(title='Локация 2')
        response = self.client.post(f'/locations/{location.id}/edit', {
            'title': 'Локация 2',
            'description': 'Новое описание',
            'lat': 15.50689,
            'lng': 32.69887
        })

        location = Location.objects.get(id=location.id)
        self.assertEquals(location.description, 'Новое описание')


class MarkerTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(username='admin', password='admin')
        self.location = Location.objects.create(user=user, title='Локация 1', description='Описание локации', lat=15.50689, lng=32.69887)
        Marker.objects.create(location=self.location, title='Маркер 1', description='Описание маркера', lat=15.50689, lng=32.69887, marker_id=123456)
        Marker.objects.create(location=self.location, title='Маркер 2', description='Описание маркера', lat=15.50689, lng=32.69887, marker_id=123456)

    def test_marker_post(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post(f'locations/{self.location.id}/marker/create', {
            'title': 'Маркер 3',
            'description': 'Описание маркера',
            'lat': 15.50689,
            'lng': 32.69887,
            'marker_id': 123456
        })

        try:
            marker = Marker.objects.filter(title='Маркер 3')
        except Marker.DoesNotExist:
            marker = None

        self.assertIsNotNone(marker)

    def test_location_delete(self):
        self.client.login(username='admin', password='admin')
        marker = Marker.objects.get(title='Маркер 1')
        response = self.client.post(f'/locations/marker/{marker.id}/delete')

        try:
            marker = Marker.objects.filter(id=marker.id)
        except Marker.DoesNotExist:
            marker = None

        self.assertIsNotNone(marker)

    def test_location_update(self):
        self.client.login(username='admin', password='admin')
        marker = Marker.objects.get(title='Маркер 2')
        response = self.client.post(f'/locations/marker/{marker.id}/edit', {
            'title': 'Маркер 2',
            'description': 'Описание маркера',
            'lat': 15.50689,
            'lng': 32.69887,
            'marker_id': 000000
        })

        marker = Marker.objects.get(id=marker.id)
        self.assertEquals(marker.marker_id, 000000)