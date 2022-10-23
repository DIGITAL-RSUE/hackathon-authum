from rest_framework import serializers

from ...models import Location


class LocationSerializer(serializers.ModelSerializer):
    """
    Сериализатор локаций
    """

    class Meta:
        model = Location
        exclude  = ["exhibitor",]
