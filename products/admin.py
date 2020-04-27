from django.contrib import admin
from.models import Product
# Register your models here.
 
class ProductAdmin(admin.ModelAdmin):
    #Creo esta clase porque no quiero mostrar el slug ya que se va a generar automaticamente
    fields = ('title', 'description', 'price', 'image')
    #mostar en el administrador aparte del title que es el str, mostrar el slug y created_at
    list_display = ('__str__', 'slug', 'created_at')

admin.site.register(Product,ProductAdmin )