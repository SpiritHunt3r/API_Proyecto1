from django.db import models


class BusRuta(models.Model):
    nombre = models.CharField(default = "", max_length=255)
    latitud_final = models.CharField(default = "", max_length=255)
    longitud_final = models.CharField(default = "", max_length=255)
    costo = models.FloatField(null=True, blank=True, default=None)
    latitud = models.FloatField(null=True, blank=True, default=None)
    longitud = models.FloatField(null=True, blank=True, default=None)
    paradas = models.ManyToManyField('busparada.BusParada')



    def __str__(self):
        return self.nombre
