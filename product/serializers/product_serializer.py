from rest_framework import serializers

from product.models import Product, Category
from .category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    categories_id = serializers.PrimaryKeyRelatedField(queryset= Category.objects.all(), many=True, write_only=True)
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'categories',
            'categories_id',
            'is_active'
        ]
    
    def create(self, validated_data):
        categories = validated_data.pop('categories_id')
        
        product = Product.objects.create(**validated_data)
        
        for category in categories: 
            product.categories.add(category)
        
        return product