from django_filters import rest_framework as filters
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

from ...models import Product
from ..serializers import ProductSerializer


class ProductFilter(filters.FilterSet):

    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        exclude = ["video","exhibitor",]

class ProductPagination(PageNumberPagination):

    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 50


class ExhibitorProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPagination
    filterset_class = ProductFilter


class ModeratorProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPagination
    filterset_class = ProductFilter
