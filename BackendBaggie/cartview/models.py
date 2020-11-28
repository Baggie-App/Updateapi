from django.db import models
from products.models import Products
from users.models import CustomUser

# Create your models here.
class CartVeiw(models.Model):
    productID    = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    customerID   = models.ForeignKey(to=CustomUser, on_delete=models.DO_NOTHING,related_name="pinfo")
    review_at    = models.DateTimeField(auto_now_add=True)
    cartstatus   = models.BooleanField(default=True)

    class Meta:
        ordering: ['-review_at']

    def __str__(self):
        return str(self.cartstatus)
