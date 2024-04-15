from django.shortcuts import render
from rest_framework import views, permissions, status
from rest_framework.response import Response

from .serializers import UserSerializer
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
