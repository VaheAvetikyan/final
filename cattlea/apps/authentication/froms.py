from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

# Translate
from django.utils.translation import gettext as _

from .models import User


# Custom Registration from extends django default
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=True, label=_("First name"))
    last_name = forms.CharField(
        max_length=30, required=True, label=_("Last name"))

    email = forms.EmailField(label=_("Email"),
                             max_length=254, required=True,
                             help_text=_('Required. Provide a valid email address.'))

    password1 = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput,
                                help_text=_("Password must contain at least 8 characters"))
    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput,
                                help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User

        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")
