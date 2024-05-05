from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        customer = Customer.objects.create_user(**validated_data)
        return customer


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Customer
        fields = (
            'username', 'password', 'password2', 'email', 'phone', 'street', 'city', 'state', 'country', 'postal_code')
        extra_kwargs = {
            'street': {'required': True},
            'city': {'required': True},
            'state': {'required': True},
            'country': {'required': True},
            'postal_code': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = Customer.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            street=validated_data['street'],
            city=validated_data['city'],
            state=validated_data['state'],
            country=validated_data['country'],
            postal_code=validated_data['postal_code'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
