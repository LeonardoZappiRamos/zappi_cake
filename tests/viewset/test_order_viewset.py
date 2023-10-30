from decimal import Decimal
import json

from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token

from django.urls import reverse

from product.factories import ProductFactory, CategoryFactory
from order.factories import OrderFactory, UserFactory
from order.models import Order

class TestOrderViewSet(APITestCase):
    client = APIClient()
    
    def setUp(self):
        self.user = UserFactory()
        
        token = Token.objects.create(user= self.user)
        token.save()
        
        self.category = CategoryFactory(name="technology")
        
        self.product_1 = ProductFactory(name="keyboard", description="new keyboard", price=50)
        self.product_2 = ProductFactory(name="mouse", description="new mouse", price=50)
        
        self.Order = OrderFactory(
            user = self.user,
            product = [self.product_1, self.product_2 ]
        )
    
    def test_get_order(self):
        token = Token.objects.get(user__username = self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        
        response = self.client.get(
            reverse('order-list', kwargs={'version': 'v1'}),
        )
        
        order = json.loads(response.content)
        
        self.assertEqual(len(order['results'][0]['products']), 2)
        self.assertEqual(order['results'][0]['user'], 1)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_order(self):
        token = Token.objects.get(user__username = self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        
        user = UserFactory()
        product = ProductFactory(name="mouse", description="new mouse", price=50)
        data = json.dumps({
            "user": user.id,
            "products_id": [product.id],
        })
        
        response = self.client.post(
            reverse('order-list', kwargs={'version': 'v1'}),
            data=data,
            content_type= 'application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        created_order = Order.objects.get(user= user.id)
        
        self.assertEqual(created_order.user, user)