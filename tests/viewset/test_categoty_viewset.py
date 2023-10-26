import json

from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from django.urls import reverse

from product.factories import CategoryFactory
from product.models import Category

class TestProductViewSet(APITestCase):
    client = APIClient()
    
    def setUp(self):
        self.category = CategoryFactory(
            name='Netbook',
            description='O melhor',   
        )

    def test_get_products(self):
        response = self.client.get(
            reverse('category-list', kwargs={'version': 'v1'}),
        )
        
        category = json.loads(response.content)
        self.assertEqual(category[0]['name'], self.category.name)
        self.assertEqual(category[0]['description'], self.category.description)
        self.assertEqual(category[0]['is_active'], self.category.is_active)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_add_products(self):
        data = json.dumps({
            "name": "Tintas",
            "description": "Tistas Diversas",
        })
        
        response = self.client.post(
            reverse('category-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )
                
        created_category = Category.objects.get(name= 'Tintas')
        
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(created_category.name, 'Tintas')
        self.assertEquals(created_category.description, 'Tistas Diversas')
