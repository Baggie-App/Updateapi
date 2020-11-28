from django.urls import path
from rest_framework.routers import SimpleRouter
from products.views import (
      ProductsListAPIView,
      ProductsDetailAPIView,
      #onlyproduct_Create,
      ProductsListWithImageAPIView,
      ProductsListWithoutAPIView,
)
#
urlpatterns = [

    #path('api/v1/create/',onlyproduct_Create, name="create"),
    path('api/v1/onlyproduct/create',ProductsListWithoutAPIView.as_view(), name="onlycreate"),
    path('api/v1/create/', ProductsListWithImageAPIView.as_view(), name="imagewithproducts"),
    path('api/v1/list', ProductsListAPIView.as_view(), name = "productsList"),
    path('api/v1/<int:id>', ProductsDetailAPIView.as_view(), name = "productsDetails"),
]
