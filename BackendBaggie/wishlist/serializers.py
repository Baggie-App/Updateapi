from rest_framework import serializers
from wishlist.models import WishList


class WishListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = WishList
        fields = ('id','productID', 'customerID', 'wish_at')



class WishlistSerializer(serializers.ModelSerializer):
    customerid   = serializers.CharField(source='customerID.id', read_only=True)
    customername = serializers.CharField(source='customerID.name', read_only=True)
    phonenumber = serializers.CharField(source='customerID.mobileNumber', read_only=True)
    email = serializers.CharField(source='customerID.email', read_only=True)

    class Meta:
        model = WishList
        fields = ('id','productID','wish_at','customerid','customername','phonenumber','email')
        depth = 1
