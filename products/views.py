from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product, Vote, Rating
from products.serializers import ProductModelSerializer, VotesModelSerializer


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


class CastVoteView(viewsets.ViewSet):
    queryset = Vote.objects.all()
    serializer_class = VotesModelSerializer

    def create(self, request, *args, **kwargs):
        rating = get_object_or_404(Rating, id=self.kwargs['id'])
        vote_value = request.data.get('vote', True)
        vote = Vote.objects.create(rating=rating, user=request.user, vote=vote_value)
        return Response(self.serializer_class(vote).data)

    def update(self, request, *args, **kwargs):
        vote = get_object_or_404(Vote, id=self.kwargs['id'])
        vote.vote = not vote.vote
        vote.save()
        return Response(self.serializer_class(vote).data)

    def destroy(self, request, *args, **kwargs):
        vote = get_object_or_404(Vote, id=self.kwargs['id'])
        vote.delete()
        return Response(status=204)


class VoteCountView(APIView):
    def get(self, request, *args, **kwargs):
        up_votes = Vote.objects.filter(rating_id=kwargs['rating_id'], vote=True).count()
        down_votes = Vote.objects.filter(rating_id=kwargs['rating_id'], vote=False).count()

        return Response({'up_votes': up_votes, 'down_votes': down_votes})
