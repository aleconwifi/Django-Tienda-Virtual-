from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product
from django.views.generic.detail import DetailView
#la clase q permite una consulta con diferentes filtros
from django.db.models import Q

class ProductListView(ListView):
    template_name = 'index.html'
    #consulta
    queryset = Product.objects.all().order_by('-id')

    #pasar el contexto de la clase al template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Productos'
        print(context)
        context['products'] = context['product_list'] 
        return context

#obtener el detalle de un producto
class ProductDetailView(DetailView):  #id va a ser de la pk
    model = Product
    template_name = 'products/product.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(context)
        return context

class ProductSearchListView(ListView):
    template_name = 'products/search.html'
    #consulta
    #queryset = Product.objects.all().order_by('-id')

    #pasar el contexto de la clase al template
    def get_queryset(self):
        filters = Q(title__icontains=self.query()) | Q(category__title__icontains=self.query())
        #SELCT * FROM products WHERE title like %valor%
        return Product.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['product_list'].count()
        print('Este es query', context['query'])
        return context