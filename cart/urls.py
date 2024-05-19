from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CartViewSet


urlpatterns = [
    # Add your URL patterns here
    path('get/<slug:id>', CartViewSet.as_view({"get":"retrieve", "post": "create", "put": "update"}), name='cart'),
]
