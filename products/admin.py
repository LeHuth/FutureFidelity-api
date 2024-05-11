from django.contrib import admin

# Register your models here.
from products.models import Category, Product, Rating, Vote
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(Vote)
