from django.shortcuts import render

# Create your views here.

def cart(request):
    #Crear una session
    request.session['cart_id'] = '123'

    #session es un diccionario, obtener su valor
    valor = request.session.get('cart_id')
    print(valor)

    #Eliminar una session
    request.session['cart_id'] = None
    #A partir de la sesion se va a trabajar con el carrito de compras, si la session se encuentra
    #en la peticion, obtenemos el carrito de compras de la base de datos, en caso contrario creamos el carrito
    return render(request, 'carts/cart.html', {


    })