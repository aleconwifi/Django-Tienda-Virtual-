from .models import Order

from django.urls import reverse


def breadcrumb(products = True, address= False, payment=False, confirmation=False):
    return [

        {'title': 'Productos', 'active': products, 'url': reverse('orders:order')},
        {'title': 'Dirección', 'active': address, 'url': reverse('orders:order')},
        {'title': 'Pago', 'active': payment, 'url': reverse('orders:order')},
        {'title': 'Confirmación', 'active': confirmation, 'url': reverse('orders:order')}
        
    ]
