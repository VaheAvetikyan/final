from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .froms import RegisterForm, LoginForm, AddressForm


# Create your views here.
def register(request):

    # If user is already authenticated, redirect to home page
    user = request.user
    if user.is_authenticated:
        return redirect("core:index")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(email=email, password=raw_password)

            login(request, user)
            return redirect("core:index")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request=request,
                          template_name="authentication/register.html",
                          context={"form": form})

    form = RegisterForm
    context = {"form": form}
    return render(request,
                  "authentication/register.html",
                  context)


def login_view(request):

    # If user is already authenticated, redirect to home page
    user = request.user
    if user.is_authenticated:
        return redirect("core:index")

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("core:index")

        else:
            messages.error(request, "Wrong Credentials")

    form = LoginForm()
    context = {"form": form}
    return render(request,
                  "authentication/login.html",
                  context)


def address(request):

    user = request.user
    
    if request.POST:
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()

        user.address = form.pk

        return redirect('carts:cart')

    form = AddressForm()
    context = {"form": form}
    return render(request,
                  "authentication/address.html",
                  context)
