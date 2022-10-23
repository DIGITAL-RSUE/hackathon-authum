from rest_framework import serializers

from ...models import Brand


class BrandSerializer(serializers.ModelSerializer):
    """
    Сериализатор брэндов
    """

    class Meta:
        model = Brand
        exclude  = ["exhibitor",]
