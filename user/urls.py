from django.urls import path, include
from .views import UserView, UserLoginView, UserLogoutView, UserSignupView, UserChangePassword, \
    UserAccountListView, UserAccountDetailView, UserAccountCreateView, UserAccountDeleteView, UserAccountUpdateView, \
    UserLocationPointListView

urlpatterns = [
    path('', UserView.as_view(), name='user'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('change_password/', UserChangePassword.as_view(), name='change_password'),

    path('accounts/', UserAccountListView.as_view(), name='accounts'),
    path('accounts/<int:pk>', UserAccountDetailView.as_view(), name='account'),
    path('accounts/<int:pk>/edit', UserAccountUpdateView.as_view(), name='account_edit'),
    path('accounts/<int:pk>/delete', UserAccountDeleteView.as_view(), name='account_delete'),
    path('accounts/create', UserAccountCreateView.as_view(), name='account_create'),

    path('points/', UserLocationPointListView.as_view(), name='points'),
]
