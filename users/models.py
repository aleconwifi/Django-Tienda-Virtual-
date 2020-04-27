from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

#SI NO SE QUIERE EXTENDER EL MODELO USER A OTRO, SINO GENERAR UNO NOSOTROS SE PUEDE USAR EL ABSTRACT USER

class User(AbstractUser):

    def get_full_name(self):
        return '{}-{}'.format(self.first_name, self.last_name)




class Customer(User):
    # proxy model es que no genere una nueva tabla en la base de datos
    class Meta:
        proxy = True
        
    def get_products(sef):
        return []


    #relacion 1 a 1 con el user con la intencion de que podamos manejar nuevos campos para el User


class Profile(models.Model):
    #CASCADE ES CUANDO UN USUARIO SEA ELIMINADO TAMBIEN SE ELIMINE SU PROFILE EN CASCADA
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField()
