from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

# Translate
from django.utils.translation import gettext_lazy as _

from .models import User, Address


# Custom Registration from extends django default
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=True, label=_("First name"),
        widget=forms.TextInput(attrs={'placeholder': _("First name"), 'class': "form-control"}))
    last_name = forms.CharField(
        max_length=30, required=True, label=_("Last name"),
        widget=forms.TextInput(attrs={'placeholder': _("Last name"), 'class': "form-control"}))

    email = forms.EmailField(label=_("Email"),
                             max_length=254, required=True,
                             help_text='Required. Provide a valid email address.',
                             widget=forms.EmailInput(attrs={'placeholder': _('Email'), 'class': "form-control"}))

    password1 = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput(attrs={'placeholder': _(
                                    'Password must be at least 8 characters.'), 'class': "form-control"}),
                                help_text=_("Password must contain at least 8 characters"))
    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': _('Confirm Password'), 'class': "form-control"}),
                                help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User

        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


class LoginForm(forms.ModelForm):
    email = forms.EmailField(label=_("Email"),
                             max_length=254, required=True,
                             help_text='Required. Provide a valid email address.',
                             widget=forms.EmailInput(attrs={'placeholder': _('Email'), 'class': "form-control"}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput(attrs={'placeholder': _('Password'), 'class': "form-control"}))

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")


class AddressForm(forms.ModelForm):

    city = forms.CharField(
        label=_("City"), max_length=64, 
        widget=forms.TextInput(attrs={'placeholder': _("City"), 'class': "form-control"})
        )

    street_address = forms.CharField(
        label=_("Street"), max_length=64,
        widget=forms.TextInput(attrs={'placeholder': _("Street"), 'class': "form-control"})
        )

    apartment_address = forms.CharField(
        label=_("Apartment"), max_length=64,
        widget=forms.TextInput(attrs={'placeholder': _("Apartment"), 'class': "form-control"})
        )

    zip = forms.CharField(
        label=_("Zip Code"), max_length=16,
        widget=forms.TextInput(attrs={'placeholder': _("Zip Code"), 'class': "form-control"})
        )

    default = forms.BooleanField(
        required=True, 
        initial=True, 
        label=_("Deafault Address")
        )


    class Meta:
        model = Address
        fields = '__all__'
