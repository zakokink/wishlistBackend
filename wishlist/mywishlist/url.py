from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('wishlist', views.WishListCreate.as_view(), name="wishlist-view-create"),
    path('wishlist/<int:userId>', views.WishListCreateByUser.as_view(), name="wishlist-view-create-user"),
    path('wishlist/<int:pk>', views.WishListEdit.as_view(), name="wishlist-edit"),
    path('categories', views.CategoryCreate.as_view(), name="category-view-create"),
    path('currencies', views.CurrencyCreate.as_view(), name="category-view-create"),
]