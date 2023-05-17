from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'GeoHeat',
        'subtitle': 'Тепловая карта публикаций в социальных сетях'
    }


class AboutView(TemplateView):
    template_name = 'main/about.html'
    extra_context = {
        'title': 'О проекте',
        'subtitle': 'Детальная информация о проекте'
    }


class TermsView(TemplateView):
    template_name = 'main/terms.html'
    extra_context = {
        'title': 'Условия использования',
        'subtitle': 'Информация об условиях использования проекта'
    }


class PrivacyView(TemplateView):
    template_name = 'main/privacy.html'
    extra_context = {
        'title': 'Политика конфиденциальности',
        'subtitle': 'Информация о политике конфиденциальности'
    }
