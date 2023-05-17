from django.urls import path
from .views import MapView, AnalyticsView

urlpatterns = [
    path('', MapView.as_view(), name='map'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
]