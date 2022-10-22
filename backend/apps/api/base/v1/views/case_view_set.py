from rest_framework import status, viewsets
from rest_framework.decorators import action

from ...models import Case
from ..serializers import CaseSerializer


class ExhibitorCaseViewSet(viewsets.ModelViewSet):
    serializer_class = CaseSerializer
    queryset = Case.objects.all()


class ModeratorCaseViewSet(viewsets.ModelViewSet):
    serializer_class = CaseSerializer
    queryset = Case.objects.all()
