from tastypie.resources import ModelResource
from bususer.models import BusUser
from tastypie.authorization import Authorization

class BusUserResource(ModelResource):
    class Meta:
        queryset = BusUser.objects.all()
        resource_name = 'user'
        authorization = Authorization()
