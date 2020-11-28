from django.urls import path
from productsImage.views import ProductImageListAPIView, ProductImageDetailAPIView


urlpatterns = [
    path('api/v1/', ProductImageListAPIView.as_view(), name = "ProductImageList"),
    path('api/v1/<int:id>', ProductImageDetailAPIView.as_view(), name = "ProductImageDetails"),
]
