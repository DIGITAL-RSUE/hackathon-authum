from rest_framework import status, viewsets
from rest_framework.decorators import action

from ...models import Brand
from ..serializers import BrandSerializer


class ModeratorBrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
