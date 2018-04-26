from tastypie.resources import ModelResource
from busruta.models import BusRuta
from tastypie.authorization import Authorization
from tastypie import fields


class BusRutaResource(ModelResource):
    paradas = fields.ManyToManyField("busparada.resources.BusParadaResource", 'paradas', 
        null=True, full=True, related_name='parada')
    class Meta:
        queryset = BusRuta.objects.all()
        resource_name = 'ruta'
        authorization = Authorization()
