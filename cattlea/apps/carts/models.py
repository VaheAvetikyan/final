from django.db import models
'''
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
'''

from cattlea.apps.authentication.models import User
from cattlea.apps.core.models import Product, Size


# Create your models here.
class CartItem(models.Model):

    # Related to User table
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Related to Shoe Size table
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=False, default=None)
    quantity = models.PositiveIntegerField()

    date_added = models.DateTimeField(verbose_name='date added', auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.item}, {self.size}, {self.quantity}, added on {self.date_added}"

    def get_price(self):
        price = item.price * self.quantity
        return price


class Cart(models.Model):

    # Related to User table
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    items = models.ManyToManyField(CartItem)

    def __str__(self):
        return f"{self.user} - {self.items}, added on {self.date_added}"

    def get_total(self):
        total = 0
        for item in self.items.all():
            total += item.get_price()
        return total
