from django.urls import path, include
from rest_framework import routers

from product import viewset

router = routers.SimpleRouter()

router.register(f'product', viewset.ProductViewSet, basename='product')
router.register(f'category', viewset.CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls))
]
