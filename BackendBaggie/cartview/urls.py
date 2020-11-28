from django.urls import path
from cartview.views import (
   CartListAPIView,
   CartDetails,
   CartUpdateAPIView,
   #OrderDestroyAPIView,
   cartDelete,
   CartCreateAPIView,
)
#
urlpatterns = [
    path('api/v1/list', CartListAPIView.as_view(), name = "cartList"),
    path('api/v1/create', CartCreateAPIView.as_view(), name = "create"),
    path('api/v1/details/<int:pk>',CartDetails, name="Detail"),
    path('api/v1/update/<int:id>', CartUpdateAPIView.as_view(), name = "cartupdate"),
    path('api/v1/delete/<int:pk>', cartDelete, name = "cartdelete"),
]
