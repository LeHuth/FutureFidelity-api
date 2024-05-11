from rest_framework import serializers

from products.models import Product, Rating, Vote


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class RatingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class VotesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
