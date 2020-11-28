from django.db import models
from products.models import Products
from users.models import CustomUser

# Create your models here.
class ProductReview(models.Model):
    productID    = models.ForeignKey(to=Products, on_delete=models.DO_NOTHING,related_name="review_product")
    customerID   = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    review       = models.CharField(max_length = 550, null=True, blank=True)
    review_at    = models.DateTimeField(auto_now_add=True)
    starreview   = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        ordering: ['-review_at']

    def __str__(self):
        return str(self.review)
