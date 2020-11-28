from orderDetails.models import OrderDetails
from orderDetails.serializers import *
from permissions import IsAuthorOrReadOnly
from headers import *
# Create your views here.
class OrderDetailsListAPIView(ListCreateAPIView):

    serializer_class = OrderDetailsSerializer
    queryset = OrderDetails.objects.all()
    lookup_field = 'id'
    # permission_classes = (permissions.IsAuthenticated,)


    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user)
    #
    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)


class OrderDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailsSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    #permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = OrderDetails.objects.all()
    lookup_field = "id"

    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)
