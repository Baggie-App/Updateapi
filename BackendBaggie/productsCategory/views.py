from productsCategory.models import ProductsCategory
from headers import *
from productsCategory.permissions import CanEditProperty
from rest_framework.decorators import api_view, permission_classes
from productsCategory.serializers import(
   ProductsCategorySerializer,
   #ProductCategoryCreateSerializer,
   ProductsCategoryforHomeSerializer,
)

class ProductsCategoryHomeListAPIView(generics.ListAPIView):

	serializer_class = ProductsCategoryforHomeSerializer
	queryset = ProductsCategory.objects.all()


# class ProductsCategoryHomeListAPIView(generics.ListAPIView):
#    serializer_class = ProductsCategorySerializer
#
#    def get_queryset(self):
#        queryset = ProductsCategory.objects.all()
#        id = self.request.query_params.getlist('id')
#        if id:
#            queryset = queryset.filter(id__in=id)
#            return queryset


class ProductsCategoryListAPIView(generics.ListCreateAPIView):
		queryset = ProductsCategory.objects.all()
		serializer_class = ProductsCategorySerializer
		filter_backends = (filters.DjangoFilterBackend,SearchFilter, OrderingFilter)
		filterset_fields = ('categoryName',)
		search_fields = ('categoryName',)

	#permission_classes = [CanEditProperty,]
	# try:
	# 	if permission_classes:
	# 		queryset = ProductsCategory.objects.all()
	# 		serializer_class = ProductsCategorySerializer
	# 		filter_backends = (filters.DjangoFilterBackend,SearchFilter, OrderingFilter)
	# 		filterset_fields = ('categoryName',)
	# 		search_fields = ('categoryName',)
	# except Exception as ex:
	# 	Response('not permission Allowed')

class ProductsCategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

	#permission_classes = [CanEditProperty,]
	queryset = ProductsCategory.objects.all()
	serializer_class = ProductsCategorySerializer
	lookup_field = "id"

# class ProductCategoryList(APIView):
#
# 	def get(self, request, format=None):
# 		productcategory = ProductsCategory.objects.all()
# 		serializer = ProductsCategorySerializer(productcategory, many=True)
# 		return Response(serializer.data)
#
# 	def post(self, request, format=None):
# 		serializer = ProductCategoryCreateSerializer(data=request.data)
# 		permission_classes = [CanEditProperty,]
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
#


	# def perform_create(self, serializer):
	# 	user = self.request.user
	# 	print(user)
	# 	if user.role=="vendor" and self.request.user == owner:
	# 		return serializer.save(owner=self.request.user)

	# def get_queryset(self):
	#     return self.queryset.filter(owner=self.request.user)
#


# class ProductsCategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView,PostUserWritePermission):
#
# 	permission_classes = [permissions.IsAuthenticated,PostUserWritePermission]
# 	queryset = ProductsCategory.objects.all()
# 	serializer_class = ProductsCategorySerializer
#
# 	lookup_field = "id"

# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# SUCCESS = 'success'
# ERROR = 'error'
# DELETE_SUCCESS = 'deleted'
# UPDATE_SUCCESS = 'updated'
# CREATE_SUCCESS = 'created'
#
# @api_view(['PUT'])
# @permission_classes((IsAuthenticated))
# def api_update_productCategory_view(request,pk):
# 	try:
# 		info_productCategory = ProductsCategory.objects.get(pk=pk)
# 	except ProductsCategory.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)
#
# 	if request.method == 'PUT':
# 		serializer = ProductsCategorySerializer(info_productCategory, data=request.data, partial=True)
# 		data = {}
# 		if serializer.is_valid():
# 			serializer.save()
# 			data['response']     = UPDATE_SUCCESS
# 			data['pk']           = info_productCategory.pk
# 			data['categoryName'] = info_productCategory.categoryName
# 			data['updated_at']   = info_productCategory.updated_at
# 			data['vendorID']        = info_productCategory.vendorID
# 			return Response(data=data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @permission_classes((IsAuthenticated,CanEditProperty,))
# def api_create_productCategory_view(request):
#
# 	if request.method == 'POST':
#
# 		print("inside create method!!!!!")
# 		data = request.data
# 		#print(data)
# 		serializerboard = ProductCategoryCreateSerializer(data=data)
#
# 		data = {}
# 		if serializerboard.is_valid():
# 			info_productCategory  = serializerboard.save()
# 			data['response']      = CREATE_SUCCESS
# 			# data['categoryName']  = info_productCategory.categoryName
# 			# data['created_at']    = info_productCategory.created_at
# 			# data['updated_at']    = info_productCategory.updated_at
# 			# data['owner']         = info_productCategory.owner
# 			return Response(data=data)
# 		return Response(serializerboard.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE',])
# @permission_classes(())
# def api_delete_productCategory_view(request, pk):
#
# 	try:
# 		info_notify = ProductsCategory.objects.get(pk=pk)
# 	except ProductsCategory.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)
#
#
# 	if request.method == 'DELETE':
# 		operation = info_notify.delete()
# 		data = {}
# 		if operation:
# 			data['response'] = DELETE_SUCCESS
# 		return Response(data=data)


#show list
# class ProductsCategoryListAPIView(ListAPIView):
# 	queryset = ProductsCategory.objects.all()
# 	serializer_class = ProductsCategorySerializer
#
# class ProductsCategorycreateAPIView(CreateAPIView):
# 	queryset = ProductsCategory.objects.all()
# 	serializer_class = ProductsCategorySerializer
# 	permission_classes = [permissions.IsAuthenticated,IsOwner,]




	# def perform_create(self, serializer):
	# 	return serializer.save(owner_ID = self.request.user)

# class ProductscategoryCreateView(generics.CreateAPIView):
# 	permissions_classes = (permissions.IsAuthenticated, IsOwner)
# 	serializer_class    = ProductCategoryCreateSerializer
# 	queryset = ProductsCategory.objects.all()
# 	filter_backends = (filters.DjangoFilterBackend,)
# 	filterset_fields = ('categoryName',)
#
# 	def perform_create(self, serializer):
# 	    return serializer.save(owner=self.request.user)




	# def get_queryset(self):
	#     return self.queryset.filter(categoryName__icontains="string")

# class SearchResultsListView(ListView):
#     model = ProductsCategory
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         print(query)
#         return ProductsCategory.objects.filter(Q(categoryName__icontains="string"))

	#context_object_name = 'book_list'
	#template_name = 'books/search_results.html'
	#
	# def get_queryset(self): # new
	#     query = self.request.GET.get('q')
	#     return Book.objects.filter(
	#         Q(title__icontains=query) | Q(author__icontains=query)
	#     )
