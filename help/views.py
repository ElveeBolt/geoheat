from django.views.generic import ListView
from .models import HelpCategory


# Create your views here.
class HelpListView(ListView):
    model = HelpCategory
    template_name = 'help/help.html'
    context_object_name = 'categories'
    extra_context = {
        'title': 'Помощь',
        'subtitle': 'Страница ответов на часто задаваемые вопросы'
    }