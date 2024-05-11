from django.db import models


class Vote(models.Model):
    user = models.ForeignKey('auth.User', related_name='vote', on_delete=models.CASCADE)
    rating = models.ForeignKey('Rating', related_name='vote', on_delete=models.CASCADE)
    vote = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.rating.product.name} - {self.user.username}'


class Rating(models.Model):
    product = models.ForeignKey('Product', related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='ratings', on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    stars = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product.name} - {self.stars} stars'


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
