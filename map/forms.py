from django import forms


class MapForm(forms.Form):
    location = forms.ModelMultipleChoiceField(
        queryset=None,
        label='Локация:',
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'placeholder': 'Выберите локацию...'
            }
        )
    )
    date_start = forms.DateTimeField(
        label='Переиод от:',
        required=True,
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ввыберите дату...',
                'type': 'datetime-local'
            }
        )
    )
    date_end = forms.DateTimeField(
        label='Период до:',
        required=True,
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ввыберите дату...',
                'type': 'datetime-local'
            }
        )
    )