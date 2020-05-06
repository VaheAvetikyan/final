import os

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

# Translate
from django.utils.translation import gettext as _

from cattlea import settings

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

        # Not working, probable TODO
        # fieldsets = [
        #     (_("Personal Information"), {
        #      "fields": ('first_name', 'last_name')}),
        #     (_("Login Information"), {
        #      "fields": ('email', 'password1', 'password2')})
        # ]

        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    '''
    TODO
    def save(self):
        # Send an email
        send_mail(
            'Welcome!',
            f'Hi {self.first_name}! Your account is created successfully․',
            settings.EMAIL_HOST_USER,
            [self.email],
            fail_silently=False,
        )

        super(User, self).save()
    '''

# Custom Login from extends django default
class LoginForm(AuthenticationForm):

    username = forms.EmailField(
        label=_(_("Email")),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'autofocus': True}))

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )
    
    class Meta:

        fields = ('username', 'password')
