from django.urls import path
from orders.views import (
   OrderListAPIView,
   ordersDetail,
   OrderUpdateAPIView,
   #OrderDestroyAPIView,
   orderDelete,
   OrderCreateAPIView,
)
#
urlpatterns = [
    path('api/v1/list', OrderListAPIView.as_view(), name = "odersList"),
    path('api/v1/create', OrderCreateAPIView.as_view(), name = "create"),
    path('api/v1/details/<int:pk>',ordersDetail, name="Detail"),
    path('api/v1/update/<int:id>', OrderUpdateAPIView.as_view(), name = "ordersupdate"),
    path('api/v1/delete/<int:pk>', orderDelete, name = "orderdelete"),
]
