from rest_framework.response import Response
from .models import Wishlist, Category, Currency
from rest_framework import generics, permissions
from .serializers import WishlistSerializer, CategorySerializer, CurrencySerializer

class WishListCreate(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all().order_by('priority')
    serializer_class = WishlistSerializer

class WishListCreateByUser(generics.ListCreateAPIView):
    serializer_class = WishlistSerializer
    def get_queryset(self):
        userId = self.kwargs.get('userId')
        return Wishlist.objects.filter(user__id=userId).order_by('priority')

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

