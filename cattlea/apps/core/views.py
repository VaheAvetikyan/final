from django.shortcuts import render

# Translate
from django.utils.translation import gettext as _

from .models import Shoe, Accessorie


# Create your views here.
def index(request):

    user = request.user
    context = {
        "menu": _("Menu"),
        "user": user
    }

    return render(request, "core/index.html", context)


def shoes(request):

    products = Shoe.objects.all()

    context = {
        "shoes": products,
    }

    return render(request, "core/shoe.html", context)


def product(request, model_code):

    prod = Shoe.objects.get(model_code=model_code)
    context = {
        "product": prod,
    }

    return render(request, "core/product.html", context)
