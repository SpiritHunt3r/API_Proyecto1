from tastypie.resources import ModelResource
from busdriver.models import BusDriver
from tastypie.authorization import Authorization
from tastypie import fields

class BusDriverResource(ModelResource):
    rutas = fields.ManyToManyField("busruta.resources.BusRutaResource", 'rutas', 
        null=True, full=True, related_name='ruta')
    class Meta:
        queryset = BusDriver.objects.all()
        resource_name = 'driver'
        authorization = Authorization()
