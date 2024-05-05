from django.urls import path, include
from rest_framework.routers import DefaultRouter

from customers.views import CustomerViewSet, CustomerSignUpView


router = DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', CustomerSignUpView.as_view(), name='signup'),
    #path('detial/<int:id>/', include(router.urls)),
]