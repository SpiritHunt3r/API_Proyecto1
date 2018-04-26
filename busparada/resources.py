from tastypie.resources import ModelResource
from busparada.models import BusParada
from tastypie.authorization import Authorization


class BusParadaResource(ModelResource):
    class Meta:
        queryset = BusParada.objects.all()
        resource_name = 'parada'
        authorization = Authorization()
