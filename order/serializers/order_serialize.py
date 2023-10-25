from rest_framework import serializers

from product.models import Product
from product.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(required=True, many=True)
    total = serializers.SerializerMethodField()
    
    def get_total(self, instance):
        total = sum([product.prize for product in instance.products.all()])
        return total
    
    class Meta:
        model = Product
        fields = [
            'products',
            'total'
        ]