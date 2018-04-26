from django.db import models

class BusDriver(models.Model):
    placa = models.CharField(default = "", max_length=255, unique = True)
    rating = models.SmallIntegerField(default=0)
    latitud = models.FloatField(null=True, blank=True, default=None)
    longitud = models.FloatField(null=True, blank=True, default=None)
    rutas = models.ManyToManyField('busruta.BusRuta')



    def __str__(self):
        return self.placa
