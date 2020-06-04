from django.urls import re_path, include

from . import views

app_name = "orders"

urlpatterns = [
    re_path(r'^place/$', views.place, name="place"),
]
