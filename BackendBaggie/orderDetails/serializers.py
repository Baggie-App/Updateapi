from rest_framework import serializers
from orderDetails.models import OrderDetails
#from users.models import CustomUser
# from orders.models import Order
# from products.models import Products

class OrderNestedDetailsSerializer(serializers.ModelSerializer):
    #orders = serializers.ReadOnlyField(source='orderID')
    #id = serializers.IntegerField(required=False)
    class Meta:
        model = OrderDetails
        fields = (
        'productID',
        'order',
        'orderDetailsName',
        'orderprice',
        'orderQuantity',
        #'orderTrakingNumber',
        'toalprice'
        )
        read_only_fields=('order',)

class OrderDetailsSerializer(serializers.ModelSerializer):
    #orders = serializers.ReadOnlyField(source='orderID')
    #id = serializers.IntegerField(required=False)
    class Meta:
        model = OrderDetails
        fields = (
        'productID',
        'order',
        'orderDetailsName',
        'orderprice',
        'orderQuantity',
        #'orderTrakingNumber',
        'toalprice'
        )
        read_only_fields=('order',)
