from django.test import Client, TestCase
from django.urls import reverse
from django.db.utils import IntegrityError

from .models import Product, Shoe, Accessorie, Size, Color


# Create your tests here.
class CoreTest(TestCase):
    def setUp(self):
        Color.objects.create(color="blue")
        Size.objects.create(size=40, size_description="26.5 cm")
        Shoe.objects.create(model_code="test1", price=20000, sex="M", style="Boots",
                            material_inner="leather", material_outer="leather", outsole="rubber",)

    def test_availability(self):
        shoe = Shoe.objects.get(pk=1)
        self.assertTrue(shoe.is_available())

    def test_prop(self):
        shoe = Shoe.objects.get(pk=1)
        self.assertEqual(shoe.style, "Boots")

    def test_insert(self):
        with self.assertRaises(IntegrityError):
            Accessorie.objects.create(model_code="test1", price=10000, sex="W", type="wallet", material="textile")

    def test_insert_1(self):
        with self.assertRaises(IntegrityError):
            Accessorie.objects.create(model_code="test2", sex="W", type="necklace", material="textile")

    def test_insert_2(self):
        try:
            Accessorie.objects.create(model_code="test2", price=10000, sex="W", type="necklace")
        except IntegrityError:
            self.fail("unexpected failure")

    # def test_index(self):
    #     c = Client()
    #     response = c.get(reverse("core:index"))
    #     self.assertEqual(response.status_code, 200)
    # TODO  image paths not recognized
