from django.db import models
from products.models import Products
from users.models import CustomUser

# Create your models here.
class WishList(models.Model):
    productID    = models.ForeignKey(to=Products, on_delete=models.DO_NOTHING,related_name="wish_info")
    customerID   = models.ForeignKey(to=CustomUser, on_delete=models.DO_NOTHING,related_name="wish_to_customer")
    wish_at      = models.DateTimeField(auto_now_add=True)
    wishtatus    = models.BooleanField(default=True)

    class Meta:
        ordering: ['-wish_at']

    def __str__(self):
        return str(self.id)
