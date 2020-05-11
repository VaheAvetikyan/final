from django.shortcuts import render
from django.http import JsonResponse

from .validation import add_or_create, show_cart


# Create your views here.
def cart(request):

    user = request.user
    items = show_cart(user)

    context = {'items': items}
    return render(request,
                  "carts/cart.html",
                  context)


def cart_add(request):

    user = request.user
    product_id = request.POST('id')
    size = request.POST('size')
    quantity = request.POST('quantity')

    ad_or_create(user, product_id, size, quantity)

    context = {}
    return JsonResponse(context)
