from rest_framework import serializers
from products.models import Products
from productsImage.models import ProductImage
from productsImage.serializers import ProductNestedImageSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
# from products.models import ProductImage
from reviewproduct.serializers import ProductReviewSerializer


class ProductNestedSerializer(serializers.ModelSerializer):
    product_image  = ProductNestedImageSerializer(many=True, read_only=True)
    review_product = ProductReviewSerializer(many=True, read_only=True)


    class Meta:
        model = Products
        fields = ('id',
        'productname',
        'productpriceoriginal',
        'productpricesell',
        'percentageofsell',
        'productweight',
        'productinstock',
        'productcoverImage',
        'productDetails',
        'productUpdate',
        'productdiscount',
        'productapprovalstatus',
        'isrecentproduct',
        'vendorID',
        'productcategoryID',
        'product_image',
        'review_product')

class ProductsSerializer(WritableNestedModelSerializer):
    # query_set = ProductImage.objects.all()
    product_image  = ProductNestedImageSerializer(many=True)
    review_product = ProductReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Products
        fields = ('id',
        'productname',
        'productpriceoriginal',
        'productpricesell',
        'percentageofsell',
        'productweight',
        'productinstock',
        'productcoverImage',
        'productDetails',
        'productUpdate',
        'productdiscount',
        'productapprovalstatus',
        'isrecentproduct',
        'vendorID',
        'productcategoryID',
        'product_image',
        'review_product')

    # def create(self, validated_data):
    #     images_data = self.context.get('view').request.FILES
    #     product = Products.objects.create(productname=validated_data.get('productname', 'no-productname'))
    #     for image_data in images_data.values():
    #         ProductImage.objects.create(image=image_data)
    #     return product


    # def create(self, validated_data):
    #     images_data = self.context.get('product_image').request.FILES
    #     product = Products.objects.create(**validated_data)
    #     for image_data in images_data:
    #         ProductImage.objects.create(**image_data, product=product)
    #     return product
    # def create(self, validated_data):
    #     images_data = self.context.get('view').request.FILES
    #     product = Products.objects.create(productName=validated_data.get('productName'),
    #                                productID_id=1)
    #     for image_data in images_data.values():
    #         ProductImage.objects.create(product=product, productImage=image_data)
    #     return product




# class ProductImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductImage
#         fields = ('image',)

# class DynamicFieldsModelSerializer(serializers.ModelSerializer):
#     """
#     A ModelSerializer that takes an additional `fields` argument that
#     controls which fields should be displayed.
#     """
#
#     def __init__(self, *args, **kwargs):
#         # Don't pass the 'fields' arg up to the superclass
#         fields = kwargs.pop('fields', None)
#
#         # Instantiate the superclass normally
#         super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)
#
#         if fields is not None:
#             # Drop any fields that are not specified in the `fields` argument.
#             allowed = set(fields)
#             existing = set(self.fields)
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)
