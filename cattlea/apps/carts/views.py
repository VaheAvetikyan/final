import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .validation import add, show_cart


# Create your views here.
def cart(request):

    user = request.user
    items = show_cart(user)

    context = {
        'items': items,
    }

    return render(request,
                  "carts/cart.html",
                  context)


@require_POST
def cart_add(request):

    user = request.user

    product = request.POST.get('product')
    size = request.POST.get('size')
    color = request.POST.get('color')
    quantity = request.POST.get('quantity')

    item = add(user, product, size, color, quantity)

    context = {'item': item.quantity}
    return JsonResponse(context)
