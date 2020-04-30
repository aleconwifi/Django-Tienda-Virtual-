from django.shortcuts import render
from products.models import Product
from django.shortcuts import redirect, get_object_or_404
from .models import Cart 
from .utils import get_or_create_cart
# Create your views here.

def cart(request):
    cart = get_or_create_cart(request)

    return render(request, 'carts/cart.html', {
        #mandando el objeto cart al template
        'cart':cart
    })

def add(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))

    #'product_id' es el nombre del formulario html donde obtiene el id del producto
    product = Product.objects.get(pk=request.POST.get('product_id'))
    #cart es una instacia del modelo por lo que para acceder a atributo products es la relacion ManytoMany
    cart.products.add(product)

    return render(request, 'carts/add.html', {
        'product': product
    })

def remove(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    #'product_id' es el nombre del formulario html donde obtiene el id del producto
    product = Product.objects.get(pk=request.POST.get('product_id'))
    #cart es una instacia del modelo por lo que para acceder a atributo products es la relacion ManytoMany
    cart.products.remove(product)

    return redirect('carts:cart')