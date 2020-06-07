from django.core.exceptions import ObjectDoesNotExist, PermissionDenied

from .models import CartItem, Cart
from cattlea.apps.authentication.models import User
from cattlea.apps.core.models import Product, Size, Color

from django.utils.translation import gettext as _


def create(user, product, size, color, quantity):

    # Create item of CartItem instance
    item = CartItem(user=user, item=product, size=size, color=color, quantity=quantity)
    item.save()

    # Django get_or_create method returns cart object or creates and returns the object
    cart, created = Cart.objects.get_or_create(user=user)
    cart.save()

    # Adds many to many field data
    cart.items.add(item)

    return item


def add(user, product, size, color, quantity):

    # Check for user authentication
    if not user.is_authenticated:
        raise PermissionDenied # ValidationError(_("Unauthorized command"), code='invalid')

    # Get models from passed in ids
    product = Product.objects.get(pk=product)

    if size == 'null':
        size = None
    else:
        try:
            size = Size.objects.get(pk=size)
        except ValueError:
            return False

    try:
        color = Color.objects.get(pk=color)
    except ValueError:
        return False

    """ 
    Try to get a CartItem object, 
    if such, add the new selected quantity,
    if not, add new object
    """
    try:
        item = CartItem.objects.get(user=user, item=product, size=size, color=color)
        item.quantity += int(quantity)
    except ObjectDoesNotExist:
        item = False

    if not item:
        item = create(user, product, size, color, quantity)

    item.save()

    return item


def show_cart(user):

    # Check for user authentication
    if not user.is_authenticated:
        raise PermissionDenied  # ValidationError(_("Unauthorized command"), code='invalid')

    items = Cart.objects.filter(user=user)

    return items


def quantify(id, operator):

    cartitem = CartItem.objects.get(pk=id)

    if operator == "plus":
        cartitem.quantity += 1
    if operator == "minus":
        cartitem.quantity -= 1

    if cartitem.quantity == 0:
        cartitem.delete()
    else:
        cartitem.save()

    return(cartitem)
