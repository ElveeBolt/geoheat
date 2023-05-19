from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView
from location.models import Location, Marker, Media, Point
from location.forms import MarkerForm, LocationForm, StartParseForm
from api.instagram import InstagramClient
from user.models import Account
from .tasks import create_task
from django.shortcuts import render



class LocationListView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'location/locations.html'
    context_object_name = 'locations'
    paginate_by = 10
    extra_context = {
        'title': 'Локации',
        'subtitle': 'Детальный список отслеживаемых локаций',
    }

    def get_queryset(self):
        return Location.objects.filter(user=self.request.user).order_by('date_publish')


class LocationDetailView(LoginRequiredMixin, FormView, DetailView):
    model = Location
    template_name = 'location/location.html'
    context_object_name = 'location'
    form_class = StartParseForm
    extra_context = {
        'title': 'Локация',
        'subtitle': 'Детальная информация касательно локации',
    }

    def get_form(self, form_class=None):
        form = StartParseForm()
        form.fields['account'].queryset = Account.objects.filter(user=self.request.user)
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['markers'] = Marker.objects.filter(location=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        account_id = request.POST.get('account')
        code = request.POST.get('code')
        account = Account.objects.get(id=account_id)
        create_task.delay(location_id=self.object.id, login=account.login, password=account.password, code=code)
        return super().post(request, *args, **kwargs)


class LocationUpdateView(LoginRequiredMixin, UpdateView):
    model = Location
    template_name = 'location/location_edit.html'
    form_class = LocationForm
    success_url = reverse_lazy('locations')
    extra_context = {
        'title': 'Редактирование локации',
        'subtitle': 'Страница редактирования данных текущей локации',
    }


class LocationCreateView(LoginRequiredMixin, CreateView):
    model = Location
    template_name = 'location/location_edit.html'
    form_class = LocationForm
    success_url = reverse_lazy('locations')
    extra_context = {
        'title': 'Добавление локации',
        'subtitle': 'Страница добавления новой локации',
    }

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LocationDeleteView(LoginRequiredMixin, DeleteView):
    model = Location
    success_url = reverse_lazy('locations')


class MarkerDetailView(LoginRequiredMixin, FormView, DetailView):
    model = Marker
    template_name = 'location/marker.html'
    context_object_name = 'marker'
    form_class = StartParseForm
    extra_context = {
        'title': 'Маркер',
        'subtitle': 'Детальная информация касательно маркера',
    }

    def get_form(self, form_class=None):
        form = StartParseForm()
        form.fields['account'].queryset = Account.objects.filter(user=self.request.user)
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['medias'] = Media.objects.filter(marker_id=self.object)
        return context


class MarkerUpdateView(LoginRequiredMixin, UpdateView):
    model = Marker
    template_name = 'location/marker_edit.html'
    form_class = MarkerForm
    success_url = reverse_lazy('locations')
    extra_context = {
        'title': 'Редактирование маркера',
        'subtitle': 'Страница редактирования данных текущего маркера',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        location = Location.objects.get(id=self.kwargs['pk'])
        points = Point.objects.filter(location=location)
        context['location'] = location
        context['points'] = points
        return context


class MarkerCreateView(LoginRequiredMixin, CreateView):
    model = Location
    template_name = 'location/marker_edit.html'
    form_class = MarkerForm
    extra_context = {
        'title': 'Добавление маркера',
        'subtitle': 'Страница добавления новой локации',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        location = Location.objects.get(id=self.kwargs['pk'])
        points = Point.objects.filter(location=location)
        context['location'] = location
        context['points'] = points
        return context

    def form_valid(self, form):
        form.instance.location = Location.objects.get(id=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('location', kwargs={'pk': self.kwargs['pk']})


class MarkerDeleteView(LoginRequiredMixin, DeleteView):
    model = Marker
    success_url = reverse_lazy('locations')




def point_list_view(request, pk):
    context = {
        'title': 'Точки',
        'subtitle': 'Детальный список полученых точек',
    }

    if request.method == 'POST':
        account_id = request.POST.get('account')
        code = request.POST.get('code')
        account = Account.objects.get(id=account_id)

        location = Location.objects.get(id=pk)

        client = InstagramClient(login=account.login, password=account.password, code=code)
        points = client.search_locations(lat=location.lat, lng=location.lng)

        if points:
            Point.objects.filter(location=location).delete()

        for point in points:
            point = Point(
                location=location,
                title=point['title'],
                address=point['address'],
                lng=point['lng'],
                lat=point['lat'],
                external_id=point['external_id']
            )
            point.save()

    context['points'] = Point.objects.filter(location_id=pk)

    return render(request, 'location/points.html', context)



# class PointListView(LoginRequiredMixin, FormView, ListView):
#     model = Point
#     template_name = 'location/points.html'
#     context_object_name = 'points'
#     form_class = StartParseForm
#     extra_context = {
#         'title': 'Точки',
#         'subtitle': 'Детальный список полученых точек',
#     }
#
#     def get_queryset(self):
#         return Point.objects.filter(location=self.kwargs['pk'])
#
#     def post(self, request, *args, **kwargs):
#         account_id = self.request.POST.get('account')
#         code = self.request.POST.get('code')
#         account = Account.objects.get(id=account_id)
#
#         location = Location.objects.get(id=self.kwargs['pk'])
#
#         client = InstagramClient(login=account.login, password=account.password, code=code)
#         points = client.search_locations(lat=location.lat, lng=location.lng)
#
#         if points:
#             Point.objects.filter(location=location).delete()
#
#         for point in points:
#             point = Point(
#                 location=location,
#                 title=point['title'],
#                 address=point['address'],
#                 lng=point['lng'],
#                 lat=point['lat'],
#                 external_id=point['external_id']
#             )
#             point.save()
#
#         return reverse_lazy('location_points', pk=self.kwargs['pk'])