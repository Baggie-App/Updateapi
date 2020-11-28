from rest_framework import serializers
from cartview.models import CartVeiw

class CartVeiwSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartVeiw
        fields = ('id','productID', 'customerID', 'review_at')
