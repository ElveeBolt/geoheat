from datetime import datetime
from celery import shared_task
from api.instagram import InstagramClient
from .models import Marker, Media


@shared_task(queue='parser')
def create_task(location_id: int, login: str, password: str, code: str):
    markers = Marker.objects.filter(location_id=location_id)
    client = InstagramClient(login=login, password=password, code=code)

    for marker in markers:
        medias = client.parse_images_by_marker(marker_id=marker.marker_id)
        for media in medias:

            if Media.objects.filter(media_pk=media.pk).exists():
                continue

            media = Media(
                media_pk=media.pk,
                marker=marker,
                code=media.code,
                description=media.caption_text,
                user_id=media.user.pk,
                username=media.user.username,
                date_publish=media.taken_at
            )
            media.save()

    return {
        'location_id': location_id
    }