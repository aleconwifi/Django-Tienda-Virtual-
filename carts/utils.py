from .models import Cart

def get_or_create_cart(request):
    #pasar todo esto a una funcion
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id') #Retorna un none en caso de que la llave no exista
    #no hacemos uso del metodo get porque se llevanta una excepcion
    cart = Cart.objects.filter(cart_id=cart_id).first() #filter retorna una lista con los elementos .first() retorna el 1ro, si no hay None

    if cart is None:
        cart = Cart.objects.create(user=user)

    if user and cart.user is None:
        cart.user = user
        cart.save()

    request.session['cart_id'] = cart.cart_id

    return cart