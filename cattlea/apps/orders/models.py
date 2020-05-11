from django.db import models

from cattlea.apps.authentication.models import User
from cattlea.apps.core.models import Product, Size


'''
ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)
'''


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=False, default=None)
    quantity = models.PositiveIntegerField()

    price = models.FloatField()

    def get_price(self):
        price = self.item.price * self.quantity
        return price

    # Automatically set the price field to keep in the order even when products price changes in the future
    def save(self, *args, **kwargs):
        self. price = self.get_price()
        super().save(*args, **kwargs)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    items = models.ManyToManyField(OrderItem)

    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)

    '''
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    '''

    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for item in self.items.all():
            total += item.get_price()
        return total


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    city = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)

    zip = models.CharField(max_length=32)

    '''
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    '''

    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'
