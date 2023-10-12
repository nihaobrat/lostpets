from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from models import Animal


class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Необязательное поле.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Необязательное поле.')
    email = forms.EmailField(max_length=254, required=True, help_text='Обязательное поле. Введите корректный email адрес.')

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', )


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('name', 'type', 'color', 'weight', 'age', 'description')