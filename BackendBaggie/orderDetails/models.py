from django.db import models
from orders.models import Order
from products.models import Products
from utils import create_new_ref_number
# Create your models here.
#related_name="orders"
class OrderDetails(models.Model):
    orderDetailsName= models.CharField(max_length=250, null=True, blank=True)
    order           = models.ForeignKey(Order, on_delete=models.CASCADE,related_name="choices")
    productID       = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    orderprice      = models.DecimalField(max_digits=150, decimal_places=3, null=False)
    orderQuantity   = models.CharField(max_length=150, null=True)
    toalprice       = models.DecimalField(max_digits=150, decimal_places=3, null=False)
    # orderTrakingNumber= models.CharField(
    #            max_length = 10,
    #            blank=True,
    #            editable=False,
    #            unique=True,
    #            default=create_new_ref_number())

    """docstring forOrderDetails."""

    def __str__(self):
        return str(self.orderDetailsName)
