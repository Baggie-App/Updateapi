from django.urls import path
from orderDetails.views import *
#
urlpatterns = [
    path('', OrderDetailsListAPIView.as_view(), name = "orderDetailsList"),
    path('<int:id>', OrderDetailsAPIView.as_view(), name = "orderDetails"),
]
