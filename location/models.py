from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(null=False, max_length=255, verbose_name='Название локации')
    lng = models.FloatField(null=False, verbose_name='Долгота')
    lat = models.FloatField(null=False, verbose_name='Широта')
    description = models.TextField(null=True, verbose_name='Описание локации')
    date_publish = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'locations'
        verbose_name = 'локация'
        verbose_name_plural = 'Локации'


class Marker(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Локация')
    title = models.CharField(null=False, max_length=255, verbose_name='Название маркера')
    lng = models.FloatField(null=False, verbose_name='Долгота')
    lat = models.FloatField(null=False, verbose_name='Широта')
    marker_id = models.BigIntegerField(null=False, verbose_name='ID маркера')
    description = models.TextField(null=True, verbose_name='Описание маркера')
    date_publish = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'markers'
        verbose_name = 'маркер'
        verbose_name_plural = 'Маркеры'


class Media(models.Model):
    media_pk = models.BigIntegerField(null=False, verbose_name='ID')
    marker = models.ForeignKey(Marker, on_delete=models.CASCADE, verbose_name='Маркер')
    code = models.CharField(null=False, max_length=255, verbose_name='Код медия')
    description = models.TextField(verbose_name='Описание')
    user_id = models.BigIntegerField(null=False, verbose_name='ID пользователя')
    username = models.CharField(null=False, max_length=255, verbose_name='Имя пользователя')
    date_publish = models.DateTimeField(verbose_name='Дата публикации')
    date_parse = models.DateTimeField(auto_now=True, verbose_name='Дата сканирования')

    def __str__(self):
        return f"{self.media_pk}"

    class Meta:
        db_table = 'media'
        verbose_name = 'медия'
        verbose_name_plural = 'Медия'
