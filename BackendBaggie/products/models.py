from django.db import models
from users.models import CustomUser
from productsCategory.models import ProductsCategory
from django.core.files import File
from PIL import Image
import os



# Create your models here.
def upload_productCoverImage(instance, filename, **kwargs):
	file_path = 'prodcutCoverImage/{productID}/{productName}-{filename}'.format(
			productID = str(instance.productID),imageName=str(instance.productname), filename=filename
		)
	return file_path

class Products(models.Model):
	CATEGORY_OPTIONS = [
		  ('is_new', 'is_new'),
		  ('not_new', 'not_new')
	  ]
	productname             = models.CharField(max_length=350, null=True)
	productpriceoriginal    = models.DecimalField(max_digits=20, decimal_places=3, null=True)
	sellproductprice        = models.DecimalField(max_digits=20, decimal_places=3, null=True)
	percentageofsell        = models.CharField(max_length = 35, null = True)
	productweight           = models.CharField(max_length = 35, null = True)
	productinstock          = models.BooleanField(default=True)
	productcoverImage       = models.ImageField(upload_to='upload_productCoverImage/',null=True, blank=True)
	productDetails          = models.TextField(null=True)
	productUpdate           = models.DateTimeField(auto_now=True)
	productdiscount         = models.BooleanField(default= False)
	productapprovalstatus   = models.BooleanField(default=False)
	isrecentproduct         = models.CharField(choices=CATEGORY_OPTIONS, max_length=100)
	vendorID                = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, null=True)
	productcategoryID       = models.ForeignKey(ProductsCategory, on_delete=models.DO_NOTHING, null=True, related_name="nested_products")

	class Meta:
		ordering: ['-productUpdate']

	def __str__(self):
		return str(self.id)

	def save(self, *args, **kwargs):

		super(Products, self).save()

		image = Image.open(self.productcoverImage)
		(width, height) = image.size
		size = ( 400, 400)
		image = image.resize(size, Image.ANTIALIAS)
		image.save(self.productcoverImage.path)
