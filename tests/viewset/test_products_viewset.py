from decimal import Decimal
import json

from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from django.urls import reverse

from product.factories import ProductFactory, CategoryFactory
from product.models import Product

class TestProductViewSet(APITestCase):
    client = APIClient()
    
    def setUp(self):
        self.product = ProductFactory(
            name='Netbook',
            price= 2500.00,   
        )

    def test_get_products(self):
        response = self.client.get(
            reverse('product-list', kwargs={'version': 'v1'}),
        )
        
        product = json.loads(response.content)
        self.assertEqual(product[0]['name'], self.product.name)
        self.assertEqual(product[0]['price'], '{0:.2f}'.format(self.product.price))
        self.assertEqual(product[0]['is_active'], self.product.is_active)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_add_products(self):
        category = CategoryFactory()
        
        data = json.dumps({
            "name": "Aparador de Onda",
            "description": "Um aparador que apara ondas",
            "price": 256.46,
            "categories_id": [category.id]
        })
        
        response = self.client.post(
            reverse('product-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )
                
        created_product = Product.objects.get(name= 'Aparador de Onda')
        
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(created_product.name, 'Aparador de Onda')
        self.assertEquals(created_product.price, Decimal('256.46'))
