from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import ProductViewSet

router = DefaultRouter()
#router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('detial/<int:id>/', ProductViewSet.as_view({'get': 'retrieve'}), name='product-detail'),
    path('list/', ProductViewSet.as_view({'get': 'list'}), name='product-list')
]