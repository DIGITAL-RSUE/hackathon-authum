from rest_framework import status, viewsets
from rest_framework.decorators import action

from ...models import Exhibitor
from ..serializers import ExhibitorSerializer

# class ExhibitorCaseViewSet(viewsets.ModelViewSet):
#     serializer_class = CaseSerializer
#     queryset = Case.objects.all()


class ModeratorExhibitorViewSet(viewsets.ModelViewSet):
    serializer_class = ExhibitorSerializer
    queryset = Exhibitor.objects.all()
