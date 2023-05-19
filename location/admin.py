from django.contrib import admin
from .models import Location, Marker, Media, Point


@admin.register(Marker)
class Marker(admin.ModelAdmin):
    list_display = ('title', 'location', 'date_publish')


@admin.register(Location)
class Location(admin.ModelAdmin):
    list_display = ('title', 'user', 'date_publish')


@admin.register(Media)
class Media(admin.ModelAdmin):
    list_display = ('media_pk', 'marker', 'username', 'date_publish', 'date_parse')


@admin.register(Point)
class Point(admin.ModelAdmin):
    list_display = ('title', 'address', 'lat', 'lng', 'external_id', 'date_publish')