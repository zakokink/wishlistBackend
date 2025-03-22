from django.contrib import admin

from .models import Wishlist, Category, Currency

# Register your models here.
admin.site.register(Wishlist)
admin.site.register(Category)
admin.site.register(Currency)