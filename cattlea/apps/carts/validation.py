from django.core.exceptions import ObjectDoesNotExist

from .models import CartItem, Cart
from cattlea.apps.authentication.models import User
from cattlea.apps.core.models import Product, Size, Color

from django.utils.translation import gettext as _


def add_or_create(user, product, size, color, quantity):

    if not user.is_authenticated:
        raise ValidationError(_("Unauthorized command"), code='invalid')

    user = User.objects.get(pk=user.id)
    product = Product.objects.get(pk=product)
    size = Size.objects.get(pk=size)
    color = Color.objects.get(pk=color)

    try:
        item = CartItem.objects.get(user=user, item=product, size=size, color=color)
    except ObjectDoesNotExist:
        item = False

    if not item:
        item = CartItem(user=user, item=product, size=size, color=color, quantity=quantity)
    else:
        item.quantity += quantity

    item.save()

    return item


def show_cart(user):

    if not user.is_authenticated:
        raise ValidationError(_("Unauthorized command"), code='invalid')

    user_id = user.id

    items = Cart.objects.filter(user=user_id)

    return items
