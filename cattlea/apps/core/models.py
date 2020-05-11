from django.db import models


male = "M"
female = "F"
SEX_CHOICES = [
    (male, "male"),
    (female, "female")
]

athletic = "Athletic"
boots = "Boots"
classic = "Classic"
STYLE_CHOICES = [
    (athletic, "athletic"),
    (boots, "boots"),
    (classic, "classic")
]


# Create your models here.

class Product(models.Model):

    model_code = models.CharField(max_length=32, unique=True)
    price = models.FloatField()

    image = models.ImageField()
    color = models.CharField(max_length=32)

    description = models.CharField(max_length=200, blank=True)
    available = models.BooleanField(default=True)

    def is_available(self):
        return self.available


class Size(models.Model):

    size = models.IntegerField()
    size_description = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.size} - {self.size_description}"


class Shoe(Product):

    sex = models.CharField(max_length=2, choices=SEX_CHOICES, default=male)

    style = models.CharField(max_length=64, choices=STYLE_CHOICES, default=classic)

    material_inner = models.CharField(max_length=64)
    material_outer = models.CharField(max_length=64)
    outsole = models.CharField(max_length=32)

    season = models.CharField(max_length=16, blank=True)

    sizes = models.ManyToManyField(Size, related_name="shoes")

    def __str__(self):
        return f"{self.model_code} {self.sex} - {self.color}, {self.material_inner}, " \
               f"{self.material_outer}, {self.outsole} : {self.price}"


class Accessorie(Product):

    type = models.CharField(max_length=64)
    material = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.model_code} - {self.type}, {self.color}, {self.material} : {self.price}"
