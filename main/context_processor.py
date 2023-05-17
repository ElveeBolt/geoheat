from django.conf import settings

def map_settings(request):
    return {
       'map_settings': {
           'token': settings.MAP_TOKEN,
           'style': settings.MAP_STYLE
       }
    }