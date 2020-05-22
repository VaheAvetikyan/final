from django.shortcuts import render, redirect

# Translate
from django.utils.translation import gettext as _

from .models import Product, Shoe, Accessorie


# Create your views here.
def index(request):

    user = request.user

    last_added = Product.objects.all()[:3]

    men_shoes = Shoe.objects.filter(sex='M').order_by('-pk')[:5]
    women_shoes = Shoe.objects.filter(sex='F').order_by('-pk')[:5]

    context = {
        'last_added': last_added,
        'men_shoes': men_shoes,
        'women_shoes': women_shoes,
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
