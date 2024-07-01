from rest_framework import serializers

from customers.models import Customer
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


class RatingListSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()
    upvotes = serializers.SerializerMethodField()
    downvotes = serializers.SerializerMethodField()

    def get_downvotes(self, obj):
        return Vote.objects.filter(rating=obj, vote=False).count()

    def get_upvotes(self, obj):
        return Vote.objects.filter(rating=obj, vote=True).count()

    def get_customer(self, obj):
        return dict(username=Customer.objects.filter(ratings=obj).first().username,image=Customer.objects.filter(ratings=obj).first().photo.url)


    class Meta:
        model = Rating
        fields = ('id','description','title','stars','customer','upvotes', 'downvotes', 'created_at')
        depth = 1
