from django.db import models
from datetime import datetime

class Currency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Wishlist(models.Model):
    name = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    priority = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
    completed = models.BooleanField(default=False)
    creationDate = models.DateField(default=datetime.now)
    def __str__(self):
        return self.name
