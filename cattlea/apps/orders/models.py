from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from cattlea.apps.authentication.models import User


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    ''' 
    Generic relations with different product tables
    https://docs.djangoproject.com/en/3.0/ref/contrib/contenttypes/#generic-relations
    '''
    product_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    product_id = models.PositiveIntegerField()
    product = GenericForeignKey('product_type', 'product_id')

    date_added = models.DateTimeField(verbose_name='date added', auto_now_add=True)
