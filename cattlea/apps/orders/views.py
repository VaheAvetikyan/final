from django.shortcuts import render, redirect

from cattlea.apps.carts.models import Cart
from .models import Order, OrderItem


# Create your views here.
def place(request):
    user = request.user
    
    cart = Cart.objects.get(user=user)

    for item in cart.items.all():
        print(item)
        order_item = OrderItem(
            user=item.user, item=item.item, size=item.size, 
            color=item.color, quantity=item.quantity
            )
        order_item.save()

    return redirect('core:index')
