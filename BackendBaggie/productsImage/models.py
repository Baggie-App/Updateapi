from django.db import models
from products.models import Products
from users.models import CustomUser
from django.conf import settings


def upload_products(instance, filename, **kwargs):
	file_path = 'prodcutsImage/{productID}/{imageName}-{filename}'.format(
			productID = str(instance.productID),imageName=str(instance.image), filename=filename
		)
	return file_path

# Create your models here.
class ProductImage(models.Model):
	imageName = models.CharField(max_length=550, null=True, blank=True)
	productID = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, related_name="product_image")
	image     = models.ImageField(upload_to="upload_products/",null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering: ['-updated_at']

	def __str__(self):
		return str(self.imageName)
