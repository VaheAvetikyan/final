from django.urls import re_path

from . import views

app_name = "core"

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    re_path(r'^assortment/(?P<param>\w+)/$', views.assort, name="assortment"),
    re_path(r'^product/(?P<model_code>\w+)/$', views.product),
]
