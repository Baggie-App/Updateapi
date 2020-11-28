from django.shortcuts import render
from reviewproduct.serializers import ProductReviewSerializer
from reviewproduct.models import ProductReview
from headers import *
from reviewproduct.permissions import *
from rest_framework.decorators import api_view, permission_classes

class ReviewListAPIView(generics.ListAPIView):
	#permission_classes = (CanCreatePermissionforCustomer,CanUpdateDeletePermissionforVendor)
	__basic_fields = ('productID','review_at','starreview')
	queryset = ProductReview.objects.all()
	serializer_class = ProductReviewSerializer
	filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
	filter_fields = __basic_fields
	search_fields = __basic_fields

class ReviewCreateAPIView(generics.CreateAPIView):
	#permission_classes = (CanCreatePermissionforCustomer,CanUpdateDeletePermissionforVendor)
	queryset = ProductReview.objects.all()
	serializer_class = ProductReviewSerializer


#single Retrive
@api_view(['GET'])
#@permission_classes((CanCreatePermissionforCustomer,CanUpdateDeletePermissionforVendor,))
def ReviewDetails(request, pk):
	try:
		carts = ProductReview.objects.get(id=pk)
	except ProductReview.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = ProductReviewSerializer(carts, many=False)
		return Response(serializer.data)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#update
class ReviewUpdateAPIView(generics.UpdateAPIView):
    #permission_classes = (CanCreatePermissionforCustomer,CanUpdateDeletePermissionforVendor,)
    serializer_class = ProductReviewSerializer
    queryset = ProductReview.objects.all()
    lookup_field = "id"

# class OrderDestroyAPIView(generics.DestroyAPIView):
# 	#permission_classes = (CanUpdateDeletePermissionforVendor,)
# 	serializer_class = OrderSerializer
# 	queryset = Order.objects.all()
# 	lookup_field = "id"

@api_view(['DELETE'])
#@permission_classes((CanUpdateDeletePermissionforVendor,))
def ReviewDelete(request, pk):
    cart = ProductReview.objects.get(id=pk)
    cart.delete()
    return Response("Order Deleted Successfully")
