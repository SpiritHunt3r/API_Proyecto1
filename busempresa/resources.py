from tastypie.resources import ModelResource
from busempresa.models import BusEmpresa
from tastypie.authorization import Authorization
from tastypie import fields

class BusEmpresaResource(ModelResource):
    choferes = fields.ManyToManyField("busdriver.resources.BusDriverResource", 'choferes', 
        null=True, full=True, related_name='chofer')
    class Meta:
        queryset = BusEmpresa.objects.all()
        resource_name = 'empresa'
        authorization = Authorization()
