from bususer.models import BusUser
from rest_framework import viewsets
from bususer.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BusUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
