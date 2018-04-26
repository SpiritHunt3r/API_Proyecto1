from bususer.models import BusUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BusUser
        fields = ('id','url','is_admin','email','first_name','last_name','chofer')



