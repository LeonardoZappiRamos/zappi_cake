from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/(?P<version>(v1|v2))/', include('product.urls')),
    re_path('api/(?P<version>(v1|v2))/', include('order.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]
