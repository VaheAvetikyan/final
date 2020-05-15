from django.urls import re_path

from . import views

app_name = "core"

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    re_path(r'^shoes/$', views.shoes, name="shoes"),
    re_path(r'^shoes/(?P<model_code>\w+)/$', views.product),
]
