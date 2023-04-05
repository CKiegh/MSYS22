from operator import truediv
from pyexpat import model
from ssl import create_default_context
from unicodedata import decimal
from django.db import models
from django.urls import set_urlconf
from django.utils import timezone

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    created_at = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()

    def getName (self):
        return self.name

    def __str__(self):
        return str(self.pk) + ":" + self.name + "-" + self.city + ", " + self.country + " created at:" + str(self.created_at)

class WaterBottle(models.Model):
    SKU = models.CharField(max_length=300)
    Brand = models.CharField(max_length=300)
    Cost = models.DecimalField(decimal_places=2, max_digits=10)
    Size = models.CharField(max_length=300)
    MouthSize = models.CharField(max_length=300)
    Color = models.CharField(max_length=300)
    Supplied_By = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    Current_Quantity = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return str(self.pk) + ":" + self.SKU + ":" + self.Brand + ", " + self.MouthSize + ", " + self.Size + ", " + self.Color + ", " + "supplied by " + str(self.Supplied_By) + ", " + str(self.Cost) + ": " + str(self.Current_Quantity) 