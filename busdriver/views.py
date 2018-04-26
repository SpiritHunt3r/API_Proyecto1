from busdriver.models import BusDriver
from rest_framework import viewsets
from busdriver.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BusDriver.objects.all().order_by('-id')
    serializer_class = UserSerializer
