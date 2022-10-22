from rest_framework import status, viewsets
from rest_framework.decorators import action

from ...models import Product
from ..serializers import ProductSerializer


class ExhibitorProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ModeratorProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
