from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Wishlist, Category
from rest_framework import generics, permissions

from .serializers import WishlistSerializer, CategorySerializer


class WishListCreate(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer


class CategoryCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
