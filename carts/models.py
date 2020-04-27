
from django.db import models
from users.models import User
from products.models import Product

# Create your models here.
class Cart(models.Model):
    #relacion uno a muchos con Usuario (no vamos a restringuir que solo los usuarios autenticados creen carritos)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    #Muchos a muchos
    products =models.ManyToManyField(Product, blank=True)
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ''
