from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

# Translate
from django.utils.translation import gettext as _

from .models import Product, Shoe, Accessorie


# Create your views here.
def index(request):

    user = request.user

    last_added = Product.objects.all().order_by('-pk')[:3]

    men_shoes = Shoe.objects.filter(sex='male').order_by('-pk')[:5]
    women_shoes = Shoe.objects.filter(sex='female').order_by('-pk')[:5]

    accessories = Accessorie.objects.all().order_by('-pk')[:5]

    context = {
        'last_added': last_added,
        'men_shoes': men_shoes,
        'women_shoes': women_shoes,
        'accessories': accessories,
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

    try:
        product = Shoe.objects.get(model_code=model_code)
    except ObjectDoesNotExist:
        product = Accessorie.objects.get(model_code=model_code)

    context = {
        "product": product,
    }

    return render(request, "core/product.html", context)
