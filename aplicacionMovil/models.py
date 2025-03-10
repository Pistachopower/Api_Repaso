from django.db import models

# Create your models here.
class AplicacionMovil(models.Model):
    nombre = models.CharField(max_length=100)
    fechaCreacion = models.DateField()
    
    def __str__(self):
        return self.nombre
