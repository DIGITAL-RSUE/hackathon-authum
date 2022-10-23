from rest_framework import status, viewsets
from rest_framework.decorators import action

from ...models import Location
from ..serializers import LocationSerializer



class ExhibitorLocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()



class ModeratorLocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
