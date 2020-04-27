from django.urls import path

from . import views

#con esto decimos que todas estas rutas son de la aplicacion products y asi nos evitamos en conflicto
#entre rutas, podemos tener dos o mas rutas con el mismo nombre
app_name = 'products'


urlpatterns = [
    path('search',views.ProductSearchListView.as_view() , name="search"),
    path('<slug:slug>',views.ProductDetailView.as_view() , name="product"),

]
