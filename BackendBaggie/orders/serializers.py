from rest_framework import serializers
from orders.models import Order
from orderDetails.serializers import OrderNestedDetailsSerializer
from orderDetails.models import OrderDetails
from drf_writable_nested.serializers import WritableNestedModelSerializer

class OrderSerializer(WritableNestedModelSerializer):
    choices  = OrderNestedDetailsSerializer(many=True)
    class Meta:
        model = Order
        fields = (
        'id',
        'customerID',
        'addressOne',
        'addressTwo',
        'city',
        'phonenumber',
        'additionalnumber',
        'orderemail',
        'orderDate',
        'orderShipped',
        'choices',
        'totalPrice')






###############################################################################
        #read_only_fields=('choices',)

        # def create(self, validated_data):
        #     choices = validated_data.pop('choices')
        #     order = Order.objects.create(**validated_data)
        #     for choice in choices:
        #         OrderDetails.objects.create(**choice, order=order)
        #     return order

        # def create(self, validated_data):
        #     order_details = validated_data.pop('choices',[])
        #     print(order_details)
        #     order = Order.objects.create(**validated_data)
        #     for order_detail in order_details:
        #         task = OrderDetails.objects.get(pk=order_detail.get('id'))
        #         order.tasks.add(task)
        #         # OrderDetails.objects.create( **order_detail, order=order)
        #     return order

        # def update(self, instance, validated_data):
        #     orders_data = validated_data.pop('orders')
        #     orders = (instance.orders).all()
        #     orders = list(orders)
        #     instance.customerID = validated_data.get('customerID', instance.customerID)
        #     instance.addressOne = validated_data.get('addressOne', instance.addressOne)
        #     instance.addressTwo = validated_data.get('addressTwo', instance.addressTwo)
        #     instance.city = validated_data.get('city', instance.city)
        #     instance.phonenumber = validated_data.get('phonenumber', instance.phonenumber)
        #     instance.additionalnumber = validated_data.get('additionalnumber', instance.additionalnumber)
        #     instance.orderemail = validated_data.get('orderemail', instance.orderemail)
        #     instance.orderDate = validated_data.get('orderDate', instance.orderDate)
        #     instance.orderShipped = validated_data.get('orderShipped', instance.orderShipped)
        #     instance.orderTrakingNumber = validated_data.get('orderTrakingNumber', instance.orderTrakingNumber)
        #
        #     instance.save()
        #     keep_od = []
        #     for order_data in orders_data:
        #         if "id" in order_data.keys():
        #             if OrderDetails.objects.filter(id=order_data["id"]).exists():
        #                 od = OrderDetails.objects.get(id=order_data["id"])
        #                 od.productID = order_data.get('productID', od.productID)
        #                 od.orderDetailsName = order_data.get('orderDetailsName', od.orderDetailsName)
        #                 od.orderprice = order_data.get('orderprice', od.orderprice)
        #                 od.orderQuantity = order_data.get('orderQuantity', od.orderQuantity)
        #                 od.toalprice = order_data.get('toalprice', od.toalprice)
        #                 od.save()
        #                 keep_od.append(od.id)
        #             else:
        #                 continue
        #         else:
        #             od = OrderDetails.objects.create(**order_data,order=instance)
        #             keep_od.append(od.id)
        #
        #     for order_data in instance.orders_data:
        #         if order_data.id not in keep_od:
        #             order_data.delete()
        #     return instance


                # order = orders.pop(0)
                # order.productID = order_data.get('productID', album.productID)
                # order.orderDetailsName = order_data.get('orderDetailsName', album.orderDetailsName)
                # order.orderprice = order_data.get('orderprice', album.orderprice)
                # order.orderQuantity = order_data.get('orderQuantity', album.orderQuantity)
                # order.toalprice = order_data.get('toalprice', album.toalprice)
                # order.save()
            # return instance
