from .models import Cart
from rest_framework import serializers


class CartSerializer(serializers.ModelSerializer):
    """
    CartSerializer is a ModelSerializer for the Cart model.
    It is used to serialize Cart objects into a format that can be easily rendered into JSON, XML, or other content types.
    It includes all fields in the Cart model.
    """

    class Meta:
        model = Cart
        fields = '__all__'
