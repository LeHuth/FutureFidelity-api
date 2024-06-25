from django.db import models


class Cart(models.Model):
    customer = models.ForeignKey('customers.Customer', related_name='cart', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', related_name='cart', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name} - {self.quantity}'

    def total(self):
        return self.product.price * self.quantity

