from rest_framework import status, viewsets
from rest_framework.decorators import action

from ...models import Producer
from ..serializers import ProducerSerializer


class ModeratorProducerViewSet(viewsets.ModelViewSet):
    serializer_class = ProducerSerializer
    queryset = Producer.objects.all()
