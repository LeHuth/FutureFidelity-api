from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from cart.models import Cart
from .serializers import CartSerializer


class CartViewSet(ViewSet):
    """
    CartViewSet is a ModelViewSet for the Cart model.
    It provides the standard actions for a RESTful API, including list, create, retrieve, update, and destroy.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = []

    def retrieve(self, request, *args, **kwargs):
        """
        Returns the details of a single Cart instance.
        """
        cart = Cart.objects.get(user_id=request.user.id)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        Updates a Cart instance.
        """
        cart = Cart.objects.get(user_id=request.user.id)
        serializer = CartSerializer(cart, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Creates a new Cart instance.
        """
        cart = Cart.objects.create(user_id=request.user.id)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class AddManyToCartView(CreateAPIView):
    """
    AddManyToCartView is a CreateAPIView for the Cart model.
    It provides a create action for a RESTful API.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = []

    def create(self, request, *args, **kwargs):

        products = request.data.get('products')

        if products is None:
            return Response({"error": "No products provided"}, status=400)

        for product in products:
            Cart.objects.create(user_id=request.user.id, product_id=product.id, quantity=product.quantiy)

        return Response({"success": "Products added to Cart"}, status=201)

