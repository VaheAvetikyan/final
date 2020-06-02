from django.test import TestCase

from .models import CartItem, Cart
from .validation import create, add, show_cart
from cattlea.apps.authentication.models import User
from cattlea.apps.core.models import Product, Shoe, Accessorie, Color, Size


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

        shoe = Shoe(model_code="test001", price=12000, sex="M", style="Athletic", material_inner="leather",
                    material_outer="leather", outsole="rubber")
        shoe.save()

        shoe.colors.add(color)
        shoe.sizes.add(size)

        cart_item = create(user, shoe, size, color, 1)

        accessory = Accessorie(model_code="test002", price=8000, sex="M", type="wallet", material="leather")
        accessory.save()

    def test_count(self):
        user = User.objects.get(pk=1)
        item = add(user=user, product=1, size=1, color=1, quantity=1)
        self.assertEqual(item.quantity, 2)

    def test_cart_count(self):
        user = User.objects.get(pk=1)
        cart = Cart.objects.get(user=user)
        cart_count = cart.get_items_count()
        self.assertEqual(cart_count, 1)

    def test_cart_count_2(self):
        user = User.objects.get(pk=1)
        add(user=user, product=2, size="null", color=1, quantity=1)
        cart = Cart.objects.get(user=user)
        cart_count = cart.get_items_count()
        self.assertEqual(cart_count, 2)

    def test_get_price(self):
        user = User.objects.get(pk=1)
        add(user=user, product=2, size=1, color=1, quantity=2)
        item = CartItem.objects.get(pk=2)
        self.assertEqual(item.get_price(), 16000)

    def test_get_total(self):
        user = User.objects.get(pk=1)
        cart = Cart.objects.get(user=user)
        self.assertEqual(cart.get_total(), 12000)
