from django.urls import path
from .views import LocationDetailView, LocationCreateView, LocationDeleteView, LocationUpdateView, LocationListView, \
    MarkerDeleteView, MarkerCreateView, MarkerDetailView, MarkerUpdateView

urlpatterns = [
    path('', LocationListView.as_view(), name='locations'),
    path('<int:pk>', LocationDetailView.as_view(), name='location'),
    path('<int:pk>/edit', LocationUpdateView.as_view(), name='location_edit'),
    path('<int:pk>/detele', LocationDeleteView.as_view(), name='location_delete'),
    path('create', LocationCreateView.as_view(), name='location_create'),

    path('marker/<int:pk>', MarkerDetailView.as_view(), name='marker'),
    path('marker/<int:pk>/edit', MarkerUpdateView.as_view(), name='marker_edit'),
    path('marker/<int:pk>/detele', MarkerDeleteView.as_view(), name='marker_delete'),
    path('<int:pk>/marker/create', MarkerCreateView.as_view(), name='marker_create'),
]