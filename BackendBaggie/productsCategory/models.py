from django.db import models


# Create your models here.
class ProductsCategory(models.Model):
    categoryName = models.CharField(max_length = 255, null=False)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering: ['-updated_at']

    def __str__(self):
        return str(self.categoryName)
