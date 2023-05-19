from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView

from location.models import Location, Marker, Media
from map.forms import MapForm


# Create your views here.
class MapView(LoginRequiredMixin, FormView, TemplateView):
    template_name = 'map/map.html'
    form_class = MapForm
    extra_context = {
        'title': 'Тепловая карта',
        'subtitle': 'Страница построения тепловой карты на основе собранных данных'
    }

    def get_form(self, form_class=None):
        form = MapForm()
        form.fields['location'].queryset = Location.objects.filter(user=self.request.user)
        return form

    def post(self, request, *args, **kwargs):
        location = request.POST.getlist('location')
        date_start = request.POST.get('date_start')
        date_end = request.POST.get('date_end')

        data = []
        location = [int(i) for i in location]

        markers = Marker.objects.filter(location_id__in=location)

        for marker in markers:
            media_count = Media.objects.filter(marker=marker, date_publish__gte=date_start, date_publish__lte=date_end).count()
            data.append({
                'marker': marker,
                'count': media_count
            })

        self.extra_context['markers'] = data

        return super().post(request, *args, **kwargs)


class AnalyticsView(LoginRequiredMixin, FormView, TemplateView):
    template_name = 'map/analytics.html'
    form_class = MapForm
    extra_context = {
        'title': 'Аналитика',
        'subtitle': 'Страница отображения аналитических данных'
    }

    def get_form(self, form_class=None):
        form = MapForm()
        form.fields['location'].queryset = Location.objects.filter(user=self.request.user)
        return form

    def post(self, request, *args, **kwargs):
        locations = request.POST.getlist('location')
        date_start = request.POST.get('date_start')
        date_end = request.POST.get('date_end')

        location_list = []
        media_list = []

        for location in locations:
            location = Location.objects.get(id=location)
            media_count = 0
            markers = Marker.objects.filter(location=location)
            for marker in markers:
                medias = Media.objects.filter(marker=marker, date_publish__gte=date_start, date_publish__lte=date_end)
                media_count += medias.count()

            location_list.append(location.title)
            media_list.append(media_count)

        self.extra_context['statistics'] = {
            'locations': {
                'labels': location_list,
                'data': media_list,
            }
        }

        return super().post(request, *args, **kwargs)