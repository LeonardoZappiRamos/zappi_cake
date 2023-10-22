from rest_framework import serializers

from models import Product

class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.ManyToManyField(required=False, allow_blank=False)
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'categories',
            'is_active'
        ]
    