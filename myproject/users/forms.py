from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import PerformerProfile, CustomerProfile


class LoginUser(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'login-form'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'login-form'}))


class RegisterForm(UserCreationForm):
    ROLE_CHOICES = [
        ('Заказчик', 'Заказчик'),
        ('Исполнитель', 'Исполнитель')
    ]

    username = forms.CharField(label="Имя пользователя")
    email = forms.EmailField(label="Электронная почта")
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput)
    role = forms.ChoiceField(label="Роль", choices=ROLE_CHOICES)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2', 'role']


class PerformerProfileForm(forms.ModelForm):
    class Meta:
        model = PerformerProfile
        fields = ['contact_info', 'experience']


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['contact_info', 'experience']
