from django.db import models
from datetime import date

class Currency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Wishlist(models.Model):
    name = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    currency = models.ForeignKey(Currency, default=1, on_delete=models.PROTECT, null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    active = models.BooleanField(default=True, null=True, blank=True)
    completed = models.BooleanField(default=False, null=True, blank=True)
    creationDate = models.DateField(default=date.today, null=True, blank=True)
    user = models.ForeignKey(User, default=1, on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return self.name + ' - ' + str(self.priority) + ' - '  + str(self.price) + ' ' + str(self.currency.name) + ' - '  + str(self.user.name)
