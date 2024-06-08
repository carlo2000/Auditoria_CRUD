from django.db import models

# Create your models here.
class Normativa(models.Model):
    tipo = models.CharField(max_length=100)
    detalle = models.CharField(max_length=200)
    descripcion = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.tipo
    