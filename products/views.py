from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductModelSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def retrieve(self, request, *args, **kwargs):
        product = get_object_or_404(self.queryset, id=self.kwargs['id'])
        return Response(self.serializer_class(product).data)

    def list(self, request, *args, **kwargs):
        products = self.queryset
        return Response(self.serializer_class(products, many=True).data)

    def get_queryset(self):
        print(self.kwargs['id'])
        product = get_object_or_404(Product, id=self.kwargs['id'])
        return product

    def get_object(self):
        return Product.objects.get(id=self.kwargs['id'])

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        return ProductModelSerializer
