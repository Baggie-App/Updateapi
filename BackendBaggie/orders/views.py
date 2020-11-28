from orders.models import Order
from orders.serializers import OrderSerializer
from headers import *
from orders.permissions import CanCreatePermissionforCustomer,CanUpdateDeletePermissionforVendor
from rest_framework.decorators import api_view, permission_classes

#list retrive
class OrderListAPIView(generics.ListAPIView):
	#permission_classes = (CanCreatePermissionforCustomer,)
	__basic_fields = ('city','phonenumber','additionalnumber','orderemail','orderDate')
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
	filter_fields = __basic_fields
	search_fields = __basic_fields

class OrderCreateAPIView(generics.CreateAPIView):
	#permission_classes = (CanCreatePermissionforCustomer,)
	queryset = Order.objects.all()
	serializer_class = OrderSerializer


#single Retrive
@api_view(['GET'])
#@permission_classes((CanCreatePermissionforCustomer,CanUpdateDeletePermissionforVendor,))
def ordersDetail(request, pk):
	try:
		orders = Order.objects.get(id=pk)
	except Order.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = OrderSerializer(orders, many=False)
		return Response(serializer.data)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#update
class OrderUpdateAPIView(generics.UpdateAPIView):
    #permission_classes = (CanUpdateDeletePermissionforVendor,)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = "id"

# class OrderDestroyAPIView(generics.DestroyAPIView):
# 	#permission_classes = (CanUpdateDeletePermissionforVendor,)
# 	serializer_class = OrderSerializer
# 	queryset = Order.objects.all()
# 	lookup_field = "id"

@api_view(['DELETE'])
#@permission_classes((CanUpdateDeletePermissionforVendor,))
def orderDelete(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return Response("Order Deleted Successfully")



#SUCCESS = 'success'
# ERROR = 'error'
# DELETE_SUCCESS = 'deleted'
#UPDATE_SUCCESS = 'updated'
# CREATE_SUCCESS = 'created'

# @api_view(['PUT'])
# def ordersUpdate(request, pk):
#     task = Order.objects.get(id=pk)
#     serializer = OrderSerializer(instance=task, data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['PUT'])
# #@permission_classes((CanUpdateDeletePermissionforVendor,))
# def api_update_order_view(request,pk):
# 	try:
# 		info_order = Order.objects.get(id=pk)
# 	except Order.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)
#
# 	if request.method == 'PUT':
# 		serializer = OrderSerializer(info_order, data=request.data, partial=True)
# 		data = {}
# 		if serializer.is_valid():
# 			serializer.save()
# 			data['response']= UPDATE_SUCCESS
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











## if loking for only method based then see ProductCategory

################################################################################
# when using only APIView
	# @action(detail=True, methods=["GET"])
	# def choices(self, request, id=None):
	#     order = self.get_object()
	#     choices = OrderDetails.objects.filter(order=order)
	#     serializer = OrderDetailsSerializer(choices, many=True)
	#     return Response(serializer.data, status=200)
	#
	# @action(detail=True, methods=["POST"])
	# def choice(self, request, id=None):
	#     order = self.get_object()
	#     data = request.data
	#     data["order"] = order.id
	#     serializer = OrderDetailsSerializer(data=data)
	#     if serializer.is_valid():
	#         serializer.save()
	#         return Response(serializer.data, status=201)
	#     return Response(serializer.erros, status=400)




	# def get_queryset(self):
	#     return self.queryset.filter(owner=self.request.user)
