from django.urls import path
from . import views

urlpatterns = [
    path('wishlist', views.WishListCreate.as_view(), name="wishlist-view-create"),
    path('wishlist/', views.WishListView.as_view(), name="wishlist-view"),
    path('wishlist/<int:userId>', views.WishListCreateByUser.as_view(), name="wishlist-view-create-user"),
    path('wishlistedit/<int:pk>', views.WishListEdit.as_view(), name="wishlist-edit"),
    path('user', views.UserView.as_view(), name="user-view-create"),
    path('user/<int:pk>', views.UserEdit.as_view(), name="user-edit"),
    path('categories', views.CategoryCreate.as_view(), name="category-view-create"),
    path('currencies', views.CurrencyCreate.as_view(), name="category-view-create"),

]