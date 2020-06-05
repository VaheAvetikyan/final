from django.shortcuts import render, redirect

from cattlea.apps.carts.models import Cart
from .models import Order, OrderItem


def place_order(user):
    """
    Creates an order and inserts all items in users shopping cart into the new order
    """

    order = Order.objects.create(user=user, shipping_address=user.address)
    cart = Cart.objects.get(user=user)

    for item in cart.items.all():
        order_item = OrderItem(
            user=item.user, item=item.item, size=item.size, 
            color=item.color, quantity=item.quantity
            )
        order_item.save()

        item.delete()

        # Add the ordered item to the order
        order.items.add(order_item)

