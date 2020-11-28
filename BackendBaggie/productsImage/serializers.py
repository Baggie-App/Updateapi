from rest_framework import serializers
from productsImage.models import ProductImage

class ProductNestedImageSerializer(serializers.ModelSerializer):
    #ownerID = serializers.ReadOnlyField(source='owner.id')
    #id = serializers.IntegerField(required=False)
    #image = serializers.ImageField(max_length=None, use_url=True, required=False)
    class Meta:
        model = ProductImage
        fields = ('id','productID','image', 'updated_at')
        read_only_fields=('productID',)

class ProductImageSerializer(serializers.ModelSerializer):
    #ownerID = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = ProductImage
        fields = ('id','productID','image', 'updated_at')
