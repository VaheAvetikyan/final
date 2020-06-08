from django.urls import re_path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = "authentication"

urlpatterns = [
    re_path(r'^register/$', views.register, name="register"),
    re_path(r'^login/$', views.login_view, name="login_view"),
    re_path(r'^account/$', views.account, name="account"),
    re_path(r'^address/$', views.address, name="address"),

    re_path(
        r'^change-password/$', 
        auth_views.PasswordChangeView.as_view(template_name='authentication/change-password.html'), 
        name="change-password"
        ),   

    re_path(r'^accounts/', include('django.contrib.auth.urls')), 
]
