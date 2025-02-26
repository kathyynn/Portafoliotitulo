from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (UserCreationForm,
                                       AuthenticationForm,
                                       PasswordResetForm,
                                       SetPasswordForm
                                       )


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Nombre de Usuario"
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Contraseña"
    }))


class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "Correo"
    }))


class NewPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(NewPasswordForm, self).__init__(*args, **kwargs)

    
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "input",
            "type": "password",
            'autocomplete': 'contraseña'
    }))

    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': "input",
            "type": "password",
            'autocomplete': 'confirma contraseña'
    }))


class UserRegistrationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Nombre de Usuario"
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "Correo"
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Contraseña"
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Confirma contraseña"
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', "password2"]

