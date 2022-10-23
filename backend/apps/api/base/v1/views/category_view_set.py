from rest_framework import status, viewsets
from rest_framework.decorators import action

from ...models import Category
from ..serializers import CategoryNestedSerializer, CategorySerializer


class ExhibitorCategoryViewSet(viewsets.ModelViewSet):
    """
    """

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ModeratorCategoryViewSet(viewsets.ModelViewSet):
    """
    """

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ExhibitorCategoryNestedViewSet(viewsets.ModelViewSet):
    """
    """

    serializer_class = CategoryNestedSerializer
    queryset = Category.objects.all()


class ModeratorCategoryNestedViewSet(viewsets.ModelViewSet):
    """
    """

    serializer_class = CategoryNestedSerializer
    queryset = Category.objects.all()
