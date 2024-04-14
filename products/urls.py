from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import ProductListView

router = DefaultRouter()
router.register(r'allProducts', ProductListView)

urlpatterns = [
    path('/', include(router.urls)),
]