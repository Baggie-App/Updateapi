from products.models import Products
from products.serializers import ProductsSerializer,ProductNestedSerializer
from headers import *
from products.permissions import CanEditPermissionForProducts
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view


# @api_view(['POST'])
# def onlyproduct_Create(request):
#     serializer = ProductNestedSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

class ProductsListWithoutAPIView(generics.CreateAPIView):
	#permission_classes = (CanEditPermissionForProducts,)
	serializer_class = ProductNestedSerializer
	queryset = Products.objects.all()

# class ProductsHomeListAPIView(generics.ListAPIView):
# 	#permission_classes = (CanEditPermissionForProducts,)
# 	#__basic_fields = ('productname','productpriceoriginal','productUpdate','isrecentproduct','vendorID__vandorName','productcategoryID__categoryName')
# 	id = ProductsCategory.objects.all()
# 	serializer_class = ProductNestedSerializer
# 	queryset = Products.objects.all()
	#filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)

	#filter_fields = __basic_fields
	#search_fields = __basic_fields

class ProductsListAPIView(generics.ListAPIView):
	#permission_classes = (CanEditPermissionForProducts,)
	__basic_fields = ('productname','productpriceoriginal','productUpdate','vendorID__vandorName','productcategoryID__categoryName')
	serializer_class = ProductNestedSerializer
	queryset = Products.objects.all().order_by('-productUpdate')
#.order_by('productname')
	filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)

	filter_fields = __basic_fields
	search_fields = __basic_fields


class ProductsListWithImageAPIView(generics.CreateAPIView):
	#permission_classes = (CanEditPermissionForProducts,)
	serializer_class = ProductsSerializer
	queryset = Products.objects.all()



class ProductsDetailAPIView(RetrieveUpdateDestroyAPIView):
	#permission_classes = (CanEditPermissionForProducts,)
	serializer_class = ProductsSerializer
	queryset = Products.objects.all()
	lookup_field = "id"

	# def get_queryset(self):
	#     return self.queryset.filter(owner=self.request.user)
