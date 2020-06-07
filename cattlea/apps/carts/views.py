import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .validation import add, show_cart, quantify
from .models import Cart


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
    if item == False:
        return JsonResponse({"status": "failed"})

    context = {
        "status": "success",
        'item': item.quantity,
    }

    return JsonResponse(context)


@require_POST
def cart_quantity(request):

    user = request.user

    id = request.POST.get("id")
    operator = request.POST.get("operator")

    cartitem = quantify(id, operator)

    total = Cart.objects.get(user=user).get_total()
    print(total)

    data = {
        "status": "success",
        "quantity": cartitem.quantity,
        "total_price": cartitem.get_price(),
        "total": total,
    }
    
    return JsonResponse(data)
