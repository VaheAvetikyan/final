from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "core"

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    re_path(r'^assortment/(?P<param>\w+)/$', views.assort, name="assortment"),
    re_path(r'^product/(?P<model_code>\w+)/$', views.product, name="product"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
