from django.urls import path
#from productsCategory.views import ProductsCategoryListAPIView, ProductsCategoryDetailAPIView
from productsCategory.views import(
    #ProductsCategoryListAPIView,
    #ProductCategoryList,
    ProductsCategoryListAPIView,
    #ProductsCategorycreateAPIView,
    #api_update_productCategory_view,
    #api_create_productCategory_view,
    #api_delete_productCategory_view,
    ProductsCategoryDetailAPIView,
    ProductsCategoryHomeListAPIView,
)
app_name = "productsCategory"
urlpatterns = [
     #path('', ProductCategoryList.as_view(), name = "List"),
     path('api/v1/alllist', ProductsCategoryHomeListAPIView.as_view(), name = "productsList"),
     path('api/v1/', ProductsCategoryListAPIView.as_view(), name = "list"),
     path('api/v1/<int:id>', ProductsCategoryDetailAPIView.as_view(), name = "pCategoryDetails"),
     #path('create/', api_create_productCategory_view, name="create"),
     #path('update/<int:pk>', api_update_productCategory_view, name="update"),
     #path('delete/<int:pk>', api_delete_productCategory_view, name="delete"),
]
