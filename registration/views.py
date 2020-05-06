from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

# Translate
from django.utils.translation import gettext as _

from .forms import RegisterForm, LoginForm


# Create your views here.

def register(request):

    # If the request is POST
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)

            print(user)
            login(request, user)
            return redirect('index')

    # If the request is GET
    else:
        form = RegisterForm
    
    # Return the registration template
    context = {"form": form}
    return render(request, "registration/register.html", context)


def login_func(request):

    # If the request is POST
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)

            login(request, user)
            return redirect('index')

    # If the request is GET
    else:
        form = LoginForm

    # Return the login template
    context = {"form": form}
    return render(request, "registration/login.html", context)