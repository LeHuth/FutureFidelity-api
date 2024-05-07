from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# Customer model that extends the auth.User model

class Customer(User):
    isSuspended = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, null=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    about = models.TextField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
