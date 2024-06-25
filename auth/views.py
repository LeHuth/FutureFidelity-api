from django.shortcuts import render
from rest_framework import views, permissions, status
from rest_framework.response import Response

from customers.models import Customer
from .serializers import UserSerializer, MeSerializer, CreateCustomerSerializer
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

class CreateUserView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserSerializer
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.token)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateCustomerView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = CreateCustomerSerializer
        if serializer.is_valid():
            customer = serializer.save()
            refresh = RefreshToken.for_user(customer)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.token)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = MeSerializer

    def get(self, request):
        customer = Customer.objects.get(id=request.user.id)
        return Response(MeSerializer(customer).data)
