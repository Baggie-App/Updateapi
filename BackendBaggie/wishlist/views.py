from django.shortcuts import render
from wishlist.serializers import WishlistSerializer,WishListCreateSerializer
from wishlist.models import WishList
from headers import *
#from cartview.permissions import *
from rest_framework.decorators import api_view, permission_classes

# Create your views here.

class WishListAPIView(generics.ListAPIView):
	#permission_classes = (CanCreatePermissionforCustomer,)
	#__basic_fields = ('city','phonenumber','additionalnumber','orderemail','orderDate')
	queryset = WishList.objects.all()
	serializer_class = WishlistSerializer
	#filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
	#filter_fields = __basic_fields
	#search_fields = __basic_fields

class WishCreateAPIView(generics.CreateAPIView):
	#permission_classes = (CanCreatePermissionforCustomer,)
	queryset = WishList.objects.all()
	serializer_class = WishListCreateSerializer


#single Retrive
@api_view(['GET'])
#@permission_classes((CanCreatePermissionforCustomer,CanUpdateDeletePermissionforVendor,))
def WishDetails(request, pk):
	try:
		carts = WishList.objects.get(id=pk)
	except WishList.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = WishlistSerializer(carts, many=False)
		return Response(serializer.data)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#update
class WishUpdateAPIView(generics.UpdateAPIView):
    #permission_classes = (CanUpdateDeletePermissionforVendor,)
    serializer_class = WishListCreateSerializer
    queryset = WishList.objects.all()
    lookup_field = "id"

# class OrderDestroyAPIView(generics.DestroyAPIView):
# 	#permission_classes = (CanUpdateDeletePermissionforVendor,)
# 	serializer_class = OrderSerializer
# 	queryset = Order.objects.all()
# 	lookup_field = "id"

@api_view(['DELETE'])
#@permission_classes((CanUpdateDeletePermissionforVendor,))
def WishDelete(request, pk):
    cart = WishList.objects.get(id=pk)
    cart.delete()
    return Response("Order Deleted Successfully")
