from django.db import models

from cattlea.apps.authentication.models import User
from cattlea.apps.core.models import Product, Size, Color


# Create your models here.
class CartItem(models.Model):

    # Related to User table
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Related to Size table
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.PositiveIntegerField()

    date_added = models.DateTimeField(verbose_name='date added', auto_now_add=True)

    def __str__(self):
        return f"{self.item} - {self.quantity}"

    def get_price(self):
        price = self.item.price * self.quantity
        return price


class Cart(models.Model):

    # Related to User table
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    items = models.ManyToManyField(CartItem)

    def __str__(self):
        return f"{self.user} - {self.items}"

    def get_total(self):
        total = 0
        for item in self.items.all():
            total += item.get_price()
        return total

    def get_items_count(self):
        return self.items.all().count()
