from instagrapi import Client


class InstagramClient:
    def __init__(self, login, password):
        self._login = login
        self.password = password

    def create_client(self):
        client = Client()
        # client.load_settings('./dump.json')
        client.login(self._login, self.password)
        client.dump_settings('./dump.json')
        return client

    def search_locations(self, lat: float, lng: float):
        client = self.create_client()
        locations = client.location_search(lat, lng)
        return self.parse_location(locations)

    def parse_location(self, locations: list):
        formated_locations = []
        for location in locations:
            location = location.dict()
            formated_locations.append({
                'name': location['name'],
                'address': location['address'],
                'lng': location['lng'],
                'lat': location['lat'],
                'id': location['external_id']
            })

        return formated_locations

    def parse_images_by_marker(self, marker_id: int):
        client = self.create_client()
        medias = client.location_medias_v1_chunk(location_pk=marker_id, tab_key='recent')
        print(medias)
        return medias[0]
