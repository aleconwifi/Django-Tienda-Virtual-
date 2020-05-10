from django.shortcuts import render
from carts.utils import get_or_create_cart
from .models import Order
from django.contrib.auth.decorators import login_required
from .utils import breadcrumb
# Create your views here.

@login_required(login_url='login')
def order(request):
    cart = get_or_create_cart(request)
    #usamos filter y no get por el probema del try exeption de la otra vez
    #order = Order.objects.filter(cart=cart).first()
    #ahora llamo a Order con el propety que defini
    order = cart.order
    #creando una orden
    if order is None and request.user.is_authenticated:
        order = Order.objects.create(cart=cart, user=request.user)
    if order:
        request.session['order_id'] = order.order_id
    print('Este es cart de order', cart)
    return render(request, 'orders/order.html', {
        'cart': cart,
        'order': order,
        'breadcrumb': breadcrumb()
    })