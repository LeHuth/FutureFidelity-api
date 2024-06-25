from rest_framework import serializers

from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

from customers.models import Customer
UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        authentication_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        print(user)
        return user



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        authentication_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        print(user)
        return user


class CreateCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user