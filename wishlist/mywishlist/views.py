from rest_framework.response import Response
from .models import Wishlist, Category, Currency, User
from rest_framework import generics, permissions
from .serializers import WishlistSerializer, CategorySerializer, CurrencySerializer, PostWishlistSerializer, \
    UserSerializer


class WishListView(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all().order_by('priority')
    serializer_class = WishlistSerializer

class WishListCreate(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all().order_by('priority')
    serializer_class = PostWishlistSerializer

class WishListCreateByUser(generics.ListCreateAPIView):
    serializer_class = WishlistSerializer
    def get_queryset(self):
        userId = self.kwargs.get('userId')
        return Wishlist.objects.filter(user__id=userId).order_by('priority')

class UserEdit(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

class WishListEdit(generics.UpdateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = PostWishlistSerializer
    lookup_field = "pk"

class WishListEdit(generics.DestroyAPIView):
    queryset = Wishlist.objects.all()
    lookup_field = "pk"


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CurrencyCreate(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

