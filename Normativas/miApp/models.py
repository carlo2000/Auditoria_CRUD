from django.db import models
from django.utils import timezone
# Create your models here.
class Normativa(models.Model):
    tipo = models.CharField(max_length=100)
    detalle = models.CharField(max_length=200)
    descripcion = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.tipo
    
    
class Comunicado(models.Model):
    tipo = models.CharField(max_length=100)
    detalle = models.CharField(max_length=200)
    descripcion = models.TextField()
    link = models.URLField()
    def __str__(self):
        return self.tipo

class Incidente(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(null=True, blank=True)
    motivo = models.TextField()
    tipo = models.CharField(max_length=100)
    severidad = models.CharField(max_length=50, choices=[
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ])
    equipo_afectado = models.CharField(max_length=200)
    descripcion_equipo_afectado = models.TextField()
    accion_tomada = models.TextField()
    fecha_accion = models.DateTimeField(null=True, blank=True)
    conclusion = models.TextField()
    recomendacion = models.TextField()

    def __str__(self):
        return f"Incidente {self.id}: {self.descripcion}"