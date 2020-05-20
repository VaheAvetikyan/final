from django.shortcuts import render, redirect

# Translate
from django.utils.translation import gettext as _

from .models import Product, Shoe, Accessorie


# Create your views here.
def index(request):

    user = request.user
    context = {
        "menu": _("Menu"),
        "user": user
    }

    return render(request, "core/index.html", context)


def assort(request, param):

    if param == "shoes":
        products = Shoe.objects.all()
    elif param == "accessories":
        products = Accessorie.objects.all()
    else:
        return redirect('core:index')

    context = {
        "products": products,
    }

    return render(request, "core/assort.html", context)


def product(request, model_code):

    prod = Product.objects.get(model_code=model_code)

    context = {
        "product": prod,
    }

    return render(request, "core/product.html", context)
