
import uuid
import decimal
from django.db import models
from users.models import User
from products.models import Product
from django.db.models.signals import pre_save
from django.db.models.signals import m2m_changed

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    #products = models.ManyToManyField(Product)
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    FEE = 0.05 #comision del 5% de la compra

    def __str__(self):
        return self.cart_id

    def update_totals(self):
        self.update_subtotal()
        self.update_total()

    def update_subtotal(self):
        self.subtotal = sum([product.price for product in self.products.all()])
        self.save() #actualzizamos en la base de datos
    
    def update_total(self):
        self.total = self.subtotal*decimal.Decimal(1+Cart.FEE)
        self.save() 


class CartProducts(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

def set_cart_id(sender, instance, *args, **kwargs):
    #si el carrito no posee un identificador unico
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())

def update_totals(sender, instance, action, *args, **kwargs):
    #cuando un producto se agrege, se elimine o el carrito se limpie
    #se calcula el subtotal y total del carrito
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.update_totals()


#callbacks
pre_save.connect(set_cart_id, sender=Cart)
m2m_changed.connect(update_totals, sender=Cart.products.through)