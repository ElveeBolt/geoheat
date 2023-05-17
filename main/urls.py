from django.urls import path
from .views import IndexView, AboutView, TermsView, PrivacyView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('terms/', TermsView.as_view(), name='terms'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
]