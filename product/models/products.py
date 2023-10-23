from django.db import models

from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=99, decimal_places=2)
    categories = models.ManyToManyField(Category, blank=True) 
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __unicode__(self):
        return self.name