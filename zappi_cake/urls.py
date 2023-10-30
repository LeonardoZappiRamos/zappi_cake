from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/(?P<version>(v1|v2))/', include('product.urls')),
    re_path('api/(?P<version>(v1|v2))/', include('order.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('api-token-auth/', views.obtain_auth_token, name="api-token-auth")
]
