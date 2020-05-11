from .models import CartItem, Cart
from django.utils.translation import gettext as _


def add_or_create(user, product_id, size, quantity):

    if not user.is_authenticated:
        raise ValidationError(_("Unauthorized command"), code='invalid')

    user_id = user.id

    item = CartItem.objects.get(user=user_id, item=product_id, size=size, quantity=quantity)
    if not item:
        item = CartItem(user=user_id, item=product_id, size=size, quantity=quantity)

    else:
        item.quantity += 1

    item.save()


def show_cart(user):

    if not user.is_authenticated:
        raise ValidationError(_("Unauthorized command"), code='invalid')

    user_id = user.id

    items = Cart.objects.filter(user=user_id)

    return items
