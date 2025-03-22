from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Wishlist, Category, Currency
from rest_framework import generics, permissions
from .serializers import WishlistSerializer, CategorySerializer, CurrencySerializer


class WishListCreate(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all().order_by('priority')
    serializer_class = WishlistSerializer


class WishListEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    lookup_field = "pk"

class CategoryCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CurrencyCreate(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

