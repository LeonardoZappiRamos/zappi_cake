from django.db import models

from django.contrib.auth.models import User
from product.models import Product

class Order(models.Model):
    products = models.ManyToManyField(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-created_at']