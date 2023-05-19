from instagrapi import Client


class InstagramClient:
    def __init__(self, login, password, code):
        self._login = login
        self.password = password
        self.code = code

    def create_client(self) -> Client:
        client = Client()
        client.login(self._login, self.password, self.code)
        return client

    def search_locations(self, lat: float, lng: float) -> list:
        client = self.create_client()
        locations = client.location_search(lat, lng)
        return self.parse_location(locations)

    def parse_location(self, locations: list) -> list:
        formated_locations = []
        for location in locations:
            location = location.dict()
            formated_locations.append({
                'title': location['name'],
                'address': location['address'],
                'lng': location['lng'],
                'lat': location['lat'],
                'external_id': location['external_id']
            })

        return formated_locations

    def parse_images_by_marker(self, marker_id: int):
        client = self.create_client()
        medias = client.location_medias_v1_chunk(location_pk=marker_id, tab_key='recent', max_amount=100)
        print(medias)
        return medias[0]
