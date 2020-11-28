from django.db import models
from users.models import CustomUser

# Create your models here.
class ProductsCategory(models.Model):
    vendorID     = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    categoryName = models.CharField(max_length = 255, null=False)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering: ['-updated_at']

    def __str__(self):
        return str(self.vendorID)
