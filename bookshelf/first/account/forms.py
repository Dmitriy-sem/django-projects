from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=25, label='', widget=forms.TextInput(
        attrs={'class': 'input100', 'placeholder': 'Имя'}))
    email = forms.EmailField(label='', widget=forms.TextInput(
        attrs={'class': 'input100', 'placeholder': 'Электронная почта'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'input100', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'input100', 'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=25, label='', widget=forms.TextInput(
        attrs={'class': 'input100', 'placeholder': 'Имя'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'input100', 'placeholder': 'Пароль'}))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control input_user', 'placeholder': 'Электронная почта'}))


class UserPhotoForm(forms.Form):
    avatar = forms.FileField(label='', widget=forms.FileInput(attrs={'class': 'input'}))


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control input_pass', 'placeholder': 'Старый пароль'}))
    new_password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control input_pass', 'placeholder': 'Новый пароль'}))
    new_password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control input_pass', 'placeholder': 'Новый пароль'}))


class PersonalInfoForm(forms.Form):
    firstname = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    lastname = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Фамилия'}))
    email = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Электронная почта'}))
