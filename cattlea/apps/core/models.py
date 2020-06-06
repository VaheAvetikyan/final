from django.db import models

# Translate
from django.utils.translation import gettext as _

male = "M"
female = "F"
SEX_CHOICES = [
    (male, _("Male")),
    (female, _("Female"))
]

athletic = _("Athletic")
boots = _("Boots")
classic = _("Classic")
STYLE_CHOICES = [
    (athletic, "athletic"),
    (boots, "boots"),
    (classic, "classic")
]


# Create your models here.
class Color(models.Model):

    color = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.color}"


class Product(models.Model):

    model_code = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=32)
    price = models.FloatField()

    sex = models.CharField(max_length=2, choices=SEX_CHOICES, default=male)

    image = models.ImageField(blank=True)
    colors = models.ManyToManyField(Color, related_name="colors")

    description = models.CharField(max_length=200, blank=True)
    available = models.BooleanField(default=True)

    def is_available(self):
        return self.available

    def __str__(self):
        return f"{self.model_code}"


class Size(models.Model):

    size = models.IntegerField()
    size_description = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.size} - {self.size_description}"


class Shoe(Product):

    style = models.CharField(max_length=64, choices=STYLE_CHOICES, default=classic)

    material_inner = models.CharField(max_length=64)
    material_outer = models.CharField(max_length=64)
    outsole = models.CharField(max_length=32)

    season = models.CharField(max_length=16, blank=True)

    sizes = models.ManyToManyField(Size, related_name="shoes")

    def __str__(self):
        return f"{self.model_code} {self.sex} - {self.material_inner}, " \
               f"{self.material_outer}, {self.outsole} : {self.price}"


class Accessorie(Product):

    type = models.CharField(max_length=64)
    material = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.model_code} - {self.type}, {self.material} : {self.price}"
