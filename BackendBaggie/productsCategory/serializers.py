from rest_framework import serializers
from productsCategory.models import ProductsCategory
from products.serializers import ProductNestedSerializer
from products.models import Products
from drf_tweaks.serializers import pass_context
from drf_tweaks.serializers import ModelSerializer


##import tant for another issue
#////////////////////////////////////////////////////////////////////
# class RelatedFieldAlternative(serializers.PrimaryKeyRelatedField):
#     def __init__(self, **kwargs):
#         self.serializer = kwargs.pop('serializer', None)
#         if self.serializer is not None and not issubclass(self.serializer, serializers.Serializer):
#             raise TypeError('"serializer" is not a valid serializer class')
#
#         super().__init__(**kwargs)
#
#     def use_pk_only_optimization(self):
#         return False if self.serializer else True
#
#     def to_representation(self, instance):
#         if self.serializer:
#             return self.serializer(instance, context=self.context).data
#         return super().to_representation(instance)

class ProductsCategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductsCategory
		fields = ('id','categoryName','created_at', 'updated_at')



class ProductsCategoryforHomeSerializer(ModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.id')
	# nested_products = serializers.SerializerMethodField()
	# print(nested_products.data)
	#nested_products = ProductNestedSerializer(many=True, read_only=True)
	#print(nested_products.data)
	#nested_products = serializers.PrimaryKeyRelatedField()
	#nested_products = RelatedFieldAlternative(queryset=Products.objects.all(), serializer=ProductNestedSerializer)
	nested_products = serializers.SerializerMethodField()

	def get_nested_products(self, instance):
		#print("hello")
		players = instance.nested_products.order_by('-productUpdate')[:10]
		return ProductNestedSerializer(players, many=True, context=self.context).data

	class Meta:
		model = ProductsCategory
		fields = ('id','categoryName','created_at', 'updated_at','nested_products')


##########################################################################################################
		# def get_nested_products(self, instance):
		# 	print("hello")
		# 	players = instance.nested_products.order_by('productname')
		# 	return ProductNestedSerializer(players, many=True, context=self.context).data
		# def to_representation(self, instance):
		# 	response = super().to_representation(instance)
		# 	response["nested_products"] = sorted(response["nested_products"], key=lambda x: x["-updated_at"])
		# 	return response


	# def get_nested_products(self, obj):
	# 	return ProductNestedSerializer(instance=obj.nested_products.order_by('productUpdate').first()).data
	#
	# def to_representation(self, obj):
	# 	"""Move fields from status to main object representation."""
	# 	representation = super().to_representation(obj)
	# 	status_representation = representation.pop('nested_products')
		#print(status_representation)
	# 	for key in status_representation:
	# 		representation[key] = status_representation[key]
	#
	# 	return representation
#######################################################################################
class ProductCategoryCreateSerializer(serializers.ModelSerializer):
	#categoryName = serializers.CharField(max_length=15, write_only=True)
	class Meta:
		model = ProductsCategory
		fields = ('id','categoryName','created_at', 'updated_at')

		def save(self):
			try:
				categoryName = self.validated_data['categoryName']
				created_at   = self.validated_data['created_at']
				updated_at   = self.validated_data['updated_at']
				# ownerID        = self.validated_data['vendorID']

				pcategory    = ProductsCategory(
							 categoryName=categoryName,
							 created_at  = created_at,
							 updated_at  = updated_at)
							 # vendorID       = vendorID)
				pcategory.save()
				return pcategory
			except KeyError:
				raise serializers.ValidationError({"reason":"something error"})
