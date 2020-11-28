from django.shortcuts import render
from cartview.serializers import CartVeiwSerializer
from cartview.models import CartVeiw
from headers import *
#from cartview.permissions import *
from rest_framework.decorators import api_view, permission_classes

# Create your views here.

class CartListAPIView(generics.ListAPIView):
	#permission_classes = (CanCreatePermissionforCustomer,)
	#__basic_fields = ('city','phonenumber','additionalnumber','orderemail','orderDate')
	queryset = CartVeiw.objects.all()
	serializer_class = CartVeiwSerializer
	#filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
	#filter_fields = __basic_fields
	#search_fields = __basic_fields

class CartCreateAPIView(generics.CreateAPIView):
	#permission_classes = (CanCreatePermissionforCustomer,)
	queryset = CartVeiw.objects.all()
	serializer_class = CartVeiwSerializer


#single Retrive
@api_view(['GET'])
#@permission_classes((CanCreatePermissionforCustomer,CanUpdateDeletePermissionforVendor,))
def CartDetails(request, pk):
	try:
		carts = CartVeiw.objects.get(id=pk)
	except CartVeiw.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = CartVeiwSerializer(carts, many=False)
		return Response(serializer.data)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#update
class CartUpdateAPIView(generics.UpdateAPIView):
    #permission_classes = (CanUpdateDeletePermissionforVendor,)
    serializer_class = CartVeiwSerializer
    queryset = CartVeiw.objects.all()
    lookup_field = "id"

# class OrderDestroyAPIView(generics.DestroyAPIView):
# 	#permission_classes = (CanUpdateDeletePermissionforVendor,)
# 	serializer_class = OrderSerializer
# 	queryset = Order.objects.all()
# 	lookup_field = "id"

@api_view(['DELETE'])
#@permission_classes((CanUpdateDeletePermissionforVendor,))
def cartDelete(request, pk):
    cart = CartVeiw.objects.get(id=pk)
    cart.delete()
    return Response("Order Deleted Successfully")
