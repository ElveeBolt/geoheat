from django.contrib import admin
from .models import Location, Marker


@admin.register(Marker)
class Marker(admin.ModelAdmin):
    list_display = ('title', 'location', 'date_publish')


@admin.register(Location)
class Location(admin.ModelAdmin):
    list_display = ('title', 'user', 'date_publish')