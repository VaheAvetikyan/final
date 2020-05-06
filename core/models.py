from django.db import models

# Translate
from django.utils.translation import gettext as _

# Create your models here.

class Item(models.Model):
    
    model_code = models.CharField(max_length=32)
    price = models.FloatField()
    color = models.CharField(max_length=32)


class Shoe(Item):

    material_inner = models.CharField(max_length=32)
    material_outer = models.CharField(max_length=32)
    outsole = models.CharField(max_length=32)

    season = models.CharField(max_length=16, blank=True)

def __str__(self):
        return f"{self.model_code} {self.sizes} - {self.color}, {self.material_inner}, {self.material_outer}, {self.outsole} : {self.price}"


class Accessorie(Item):

    material = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.model_code} - {self.color}, {self.material} : {self.price}"


class Size(models.Model):

    size = models.IntegerField()
    size_description = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.size} - {self.size_description}"


class ShoeSize(models.Model):

    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE, related_name="sizes")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="shoes")

    def __str__(self):
        return f"{self.shoe} - {self.size}"
