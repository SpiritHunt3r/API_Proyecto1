from django.db import models


class BusEmpresa(models.Model):
    nombre = models.CharField(default = "", max_length=255)
    descripcion = models.CharField(default = "", max_length=255)
    choferes = models.ManyToManyField ('busdriver.BusDriver')
    
    def __str__(self):
        return self.nombre
