from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.conf import settings
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView

from location.models import Point, Location
from user.forms import SignupForm, ChangePasswordForm, AccountForm
from .forms import LoginForm
from .models import Account


class UserView(LoginRequiredMixin, TemplateView):
    template_name = 'user/user.html'
    extra_context = {
        'title': 'Профиль',
        'subtitle': 'Детали моего профиля',
    }


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = reverse_lazy('user/manager')
    redirect_authenticated_user = True
    extra_context = {
        'title': 'Авторизация',
        'subtitle': 'Для того, чтобы использовать сервис выполните авторизацию',
    }


class UserSignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('login')
    extra_context = {
        'title': 'Регистрация профиля',
        'subtitle': 'Создайте профиль для того, чтобы использовать GeoHeat',
    }

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('user')
        else:
            return super().dispatch(request, *args, **kwargs)


class UserChangePassword(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    template_name = 'user/change_password.html'
    form_class = ChangePasswordForm
    success_url = 'change_password'
    success_message = 'Пароль успешно изменён. Во время следующей авторизации воспользуйтесь новым паролем'
    extra_context = {
        'title': 'Смена пароля',
        'subtitle': 'Страница смены пароля',
    }


class UserAccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = 'user/account_list.html'
    context_object_name = 'accounts'
    extra_context = {
        'title': 'Аккаунты социальных сетей',
        'subtitle': 'Список ваших аккаунтов',
    }


class UserAccountDetailView(LoginRequiredMixin, DetailView):
    model = Account
    template_name = 'user/account.html'
    context_object_name = 'account'
    extra_context = {
        'title': 'Аккаунт',
        'subtitle': 'Детальная информация касательно аккаунта',
    }


class UserAccountUpdateView(LoginRequiredMixin, UpdateView):
    model = Account
    template_name = 'user/account_edit.html'
    form_class = AccountForm
    success_url = reverse_lazy('accounts')
    extra_context = {
        'title': 'Редактирование аккаунта',
        'subtitle': 'Страница редактирования данных текущего аккаунта',
    }


class UserAccountCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Account
    template_name = 'user/account_edit.html'
    form_class = AccountForm
    success_url = reverse_lazy('accounts')
    success_message = 'Аккаунт успешно успешно создан. Теперь вы можете использовать его для сканирования локаций.'
    extra_context = {
        'title': 'Добавление аккаунта',
        'subtitle': 'Страница добавления нового аккаунта',
    }

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserAccountDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Account
    success_url = reverse_lazy('accounts')
    success_message = 'Аккаунт был успешно удалён.'


class UserLocationPointListView(LoginRequiredMixin, ListView):
    model = Point
    template_name = 'user/point_list.html'
    context_object_name = 'points'
    extra_context = {
        'title': 'Мои точки',
        'subtitle': 'Список ваших точек, которые были получены с локаций',
    }

    def get_queryset(self):
        locations = Location.objects.filter(user=self.request.user).values('id')
        return Point.objects.filter(location_id__in=locations)


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL
