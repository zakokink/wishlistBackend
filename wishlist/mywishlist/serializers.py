from rest_framework import serializers
from .models import Category, Currency, Wishlist, User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class WishlistSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField(read_only=False)
    currency = serializers.SerializerMethodField(read_only=False)
    user = serializers.SerializerMethodField(read_only=False)

    def get_category(self, wishlist):
        return CategorySerializer(wishlist.category, many=False, read_only=False).data

    def get_currency(self, wishlist):
        return CurrencySerializer(wishlist.currency, many=False, read_only=False).data

    def get_user(self, wishlist):
        return UserSerializer(wishlist.user, many=False, read_only=False).data

    class Meta:
        model = Wishlist
        fields = "__all__"


class PostWishlistSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    currency = serializers.PrimaryKeyRelatedField(queryset=Currency.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def get_category(self, wishlist):
        return CategorySerializer(wishlist.category, many=False, read_only=False).data

    def get_currency(self, wishlist):
        return CurrencySerializer(wishlist.currency, many=False, read_only=False).data

    def get_user(self, wishlist):
        return UserSerializer(wishlist.user, many=False, read_only=False).data

    class Meta:
        model = Wishlist
        fields = "__all__"



