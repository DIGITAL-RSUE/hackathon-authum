from rest_framework import status, viewsets
from rest_framework.decorators import action

from ...models import Partner
from ..serializers import PartnerSerializer



class ExhibitorPartnerViewSet(viewsets.ModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()



class ModeratorPartnerViewSet(viewsets.ModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()
