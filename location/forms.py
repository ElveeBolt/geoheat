from django import forms
from .models import Location, Marker


class LocationForm(forms.ModelForm):
    title = forms.CharField(
        label='Название локации:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите название...'
            }
        )
    )
    description = forms.CharField(
        label='Описание:',
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание...',
                'rows': 3
            }
        )
    )
    lat = forms.CharField(
        label='Широта:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите широту...'
            }
        )
    )
    lng = forms.CharField(
        label='Долгота:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите долготу...'
            }
        )
    )

    class Meta:
        model = Location
        fields = ['title', 'description', 'lat', 'lng']


class MarkerForm(forms.ModelForm):
    title = forms.CharField(
        label='Название маркера:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите название...'
            }
        )
    )
    description = forms.CharField(
        label='Описание маркера:',
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание...',
                'rows': 3
            }
        )
    )
    lat = forms.CharField(
        label='Широта:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите широту...'
            }
        )
    )
    lng = forms.CharField(
        label='Долгота:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите долготу...'
            }
        )
    )
    marker_id = forms.IntegerField(
        label='Идентификатор маркера:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите идентификатор...'
            }
        )
    )

    class Meta:
        model = Marker
        fields = ['title', 'description', 'lat', 'lng', 'marker_id']


class StartParseForm(forms.Form):
    account = forms.ModelChoiceField(
        label='Аккаунт:',
        queryset=None,
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'placeholder': 'Выберите аккаунт...'
            }
        )
    )

    class Meta:
        model = Marker
        fields = ['account']