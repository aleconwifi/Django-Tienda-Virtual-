from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from .forms import RegisterForm
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html', {
        #contexto
        'message': 'Listado de produtos',
        'title': 'Productos',
        'products': [
            {'title': 'zapato deportivo', 'price': '100', 'stock': True},
            {'title': 'Camisa', 'price': '60', 'stock': True},
            {'title': 'Camisa S', 'price': '60', 'stock': False},

        ]
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
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no validos')
    return render(request, 'users/login.html', {

    })


