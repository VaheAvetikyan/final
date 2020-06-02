from django.test import TestCase

from .models import CartItem, Cart
from .validation import create, add, show_cart
from cattlea.apps.authentication.models import User
from cattlea.apps.core.models import Shoe, Color, Size


# Create your tests here.
class CartTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(email="test@mail.com", first_name="test", last_name="test",
                                        password="password123")
        user.save()
        color = Color(color="yellow")
        color.save()
        size = Size(size=39, size_description="25.5 cm")
        size.save()
        product = Shoe(model_code="test001", price=12000, sex="M", style="Athletic", material_inner="leather",
                       material_outer="leather", outsole="rubber")
        product.save()
        product.colors.add(color)
        product.sizes.add(size)
        cart_item = create(user, product, size, color, 1)

    def test_count(self):
        user = User.objects.get(pk=1)
        item = add(user=user, product=1, size=1, color=1, quantity=1)
        self.assertEqual(item.quantity, 2)
