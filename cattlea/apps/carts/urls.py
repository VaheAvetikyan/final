from django.urls import re_path, include

from . import views

app_name = "carts"

urlpatterns = [
    re_path(r'^$', views.cart, name="cart"),
    re_path(r'^add/$', views.cart_add, name="add"),
    re_path(r'^quant/$', views.cart_quantity, name="quantity"),
]
