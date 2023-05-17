from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    NETWORK_CHOICES = [
        ('instagram', 'instagram'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    login = models.CharField(null=False, max_length=255, verbose_name='Логин')
    password = models.CharField(null=False, max_length=255, verbose_name='Пароль')
    network = models.CharField(null=False, max_length=255, choices=NETWORK_CHOICES, default='instagram', verbose_name='Социальная сеть')
    comment = models.TextField(null=True, verbose_name='Комментарий')
    date_publish = models.DateTimeField(auto_now=True, verbose_name='Дата добавления')

    def __str__(self):
        return f"{self.login}"

    class Meta:
        db_table = 'accounts'
        verbose_name = 'аккаунт'
        verbose_name_plural = 'Аккаунты'
