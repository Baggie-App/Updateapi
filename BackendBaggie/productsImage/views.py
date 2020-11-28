from django.shortcuts import render
from productsImage.serializers import ProductImageSerializer
from productsImage.models import ProductImage
#from permissions import IsOwner,IsAuthorOrReadOnly,IsAdminUser
from headers import *

# Create your views here.
class ProductImageListAPIView(ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,IsAuthorOrReadOnly,)
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()
    #lookup_field = "id"


    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user)

    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)


class ProductImageDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductImageSerializer
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = ProductImage.objects.all()
    lookup_field = "id"
