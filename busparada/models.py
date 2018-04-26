from django.db import models


class BusParada(models.Model):
    nombre = models.CharField(default = "", max_length=255)    
    latitud = models.FloatField(null=True, blank=True, default=None)
    longitud = models.FloatField(null=True, blank=True, default=None)
    
    def __str__(self):
        return self.nombre
