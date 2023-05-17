from django.db import models


# Create your models here.
class HelpCategory(models.Model):
    title = models.CharField(null=False, max_length=255, verbose_name='Название категории')
    description = models.TextField(null=True, verbose_name='Описание категории')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


# Create your models here.
class Help(models.Model):
    category = models.ForeignKey(HelpCategory, on_delete=models.CASCADE, verbose_name='Категория')
    question = models.CharField(null=False, max_length=255, verbose_name='Вопрос')
    answer = models.TextField(null=False, verbose_name='Ответ')

    def __str__(self):
        return f"{self.question}"

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'Вопросы'
