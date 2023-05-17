from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

from user.models import Account


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин...'
            }
        )
    )
    password = forms.CharField(
        label='Пароль:',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль...'
            }
        )
    )


class SignupForm(UserCreationForm):
    username = forms.CharField(
        label='Логин:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин...'
            }
        )
    )
    email = forms.CharField(
        label='E-mail:',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите e-mail...'
            }
        )
    )
    password1 = forms.CharField(
        label='Пароль:',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль...'
            }
        )
    )
    password2 = forms.CharField(
        label='Повторите пароль:',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль...'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        required=True,
        label='Текущий пароль:',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Введите текущий пароль...',
                'class': 'form-control'
            }
        )
    )
    new_password1 = forms.CharField(
        required=True,
        label='Новый пароль:',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Введите пароль...',
                'class': 'form-control'
            }
        )
    )
    new_password2 = forms.CharField(
        required=True,
        label='Повторите пароль:',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Повторите пароль...',
                'class': 'form-control'
            }
        )
    )


class AccountForm(forms.ModelForm):
    login = forms.CharField(
        required=True,
        label='Логин:',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите логин...',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        required=True,
        label='Пароль:',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Введите пароль...',
                'class': 'form-control'
            }
        )
    )
    network = forms.ChoiceField(
        choices=Account.NETWORK_CHOICES,
        required=True,
        label='Социальная сеть:',
        widget=forms.Select(
            attrs={
                'placeholder': 'Выберите сеть...',
                'class': 'form-select'
            }
        )
    )

    comment = forms.CharField(
        label='Комментарий:',
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите комментарий...',
                'rows': 3
            }
        )
    )

    class Meta:
        model = Account
        fields = ['login', 'password', 'network', 'comment']