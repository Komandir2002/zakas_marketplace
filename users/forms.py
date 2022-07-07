from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
)
from django.forms import EmailField
from .models import CustomUser


class RegisterationForm(UserCreationForm):
    GENDER_TYPE = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"))
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    email = forms.EmailField(required=True)
    birth_day = forms.DateField(required=True)
    phone_number = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "gender",
            "birth_day",
            "phone_number",
        ]

    def save(self, commit=True):
        user = super(RegisterationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "please type user username...",
                "id": "username",
            }
        )
    )

    email = EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "please type user email...",
                "id": "email",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "please type user password...",
                "id": "password",
            }
        )
    )