from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from .forms import RegisterForm
#from django.contrib.auth.models import User
from products.models import Product
from users.models import User

#Vistas basadas en clases. Agilizas el proceso porque usas django, mover a view del proyecto

def index(request):
    products = Product.objects.all().order_by('-id')

    return render(request, 'index.html', {
        #contexto
        'message': 'Listado de produtos',
        'title': 'Productos',
        'products': products,
        })



def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('login')


def register(request):
    #si el usuario esta atenticado voy a redirigir a index
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():

        #cleaned_data es un diccionario
        #username = form.cleaned_data.get('username')
        #email = form.cleaned_data.get('email')
        #password = form.cleaned_data.get('password')
        #AHORA OBTENGO ESTO DEL METODO DEL FORM 
        user = form.save()

        #user = User.objects.create_user(username=username, email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')

    return render(request, 'users/register.html', {
        'form': form
    })

@csrf_protect
def login_view(request):
    #si el usuario esta atenticado voy a redirigir a index
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username') #es un diccionario con dos llaves con .get obtenemos una llave si existe
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            #si la peticion posee el parametro next hacemos un redirect
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'] )
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no validos')
    return render(request, 'users/login.html', {

    })


