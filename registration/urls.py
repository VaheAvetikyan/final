from django.urls import path

from . import views

app_name = "registration"

urlpatterns = [
    path("", views.register, name="register"),
    path("login/", views.login_func, name="login"),
]
