from django.db import models

from category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    prize = models.DecimalField(decimal_places=2)
    categories = models.ManyToManyField(Category, on_delete=models.CASCADE) 
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name