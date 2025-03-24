from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
)  # agregamos estos para la autenticacion
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.
class Usuario(AbstractUser):
    # clave-valor:
    # abajo están los usuarios que vamos a crear
    ADMINISTRADOR = 1
    CREADOR_APP = 2
    CLIENTE = 3
    ROLES = [
        (ADMINISTRADOR, "administrador"),
        (CREADOR_APP, "creador_app"),
        (CLIENTE, "cliente"),
    ]

    #cuando un usuario se crea por defecto es administrador (preguntar)
    rol = models.PositiveSmallIntegerField(choices=ROLES, default=1)


class AplicacionMovil(models.Model):
    nombre = models.CharField(max_length=100)
    fechaCreacion = models.DateField()
    
    def __str__(self):
        return self.nombre
    

class Comentario(models.Model):
    texto_comentario= models.TextField()
    aplicacion_movil= models.ForeignKey(AplicacionMovil, on_delete=models.CASCADE, related_name='comentarios')
    puntuacion= models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario')
    fecha_comentario = models.DateField()
