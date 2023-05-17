from django.contrib import admin
from .models import Help, HelpCategory


@admin.register(Help)
class Help(admin.ModelAdmin):
    list_display = ('question', 'category')


@admin.register(HelpCategory)
class HelpCategory(admin.ModelAdmin):
    list_display = ('title',)