from django.urls import path
from wishlist.views import (
   WishListAPIView,
   WishDetails,
   WishUpdateAPIView,
   WishDelete,
   WishCreateAPIView,
)
#
urlpatterns = [
    path('api/v1/list', WishListAPIView.as_view(), name = "cartList"),
    path('api/v1/create', WishCreateAPIView.as_view(), name = "create"),
    path('api/v1/details/<int:pk>',WishDetails, name="Detail"),
    path('api/v1/update/<int:id>', WishUpdateAPIView.as_view(), name = "cartupdate"),
    path('api/v1/delete/<int:pk>', WishDelete, name = "cartdelete"),
]
