from django.urls import path, include
from rest_framework import routers

from order import viewset

router = routers.SimpleRouter()

router.register(f'order', viewset.OrderViewset, basename='order')

urlpatterns = [
    path('', include(router.urls))
]
