from django.urls import path
from reviewproduct.views import (
   ReviewListAPIView,
   ReviewDetails,
   ReviewUpdateAPIView,
   ReviewDelete,
   ReviewCreateAPIView,
)
#
urlpatterns = [
    path('api/v1/list', ReviewListAPIView.as_view(), name = "List"),
    path('api/v1/create', ReviewCreateAPIView.as_view(), name = "create"),
    path('api/v1/details/<int:pk>',ReviewDetails, name="Detail"),
    path('api/v1/update/<int:id>', ReviewUpdateAPIView.as_view(), name = "update"),
    path('api/v1/delete/<int:pk>', ReviewDelete, name = "delete"),
]
