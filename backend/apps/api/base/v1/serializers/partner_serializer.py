from rest_framework import serializers

from ...models import Partner


class PartnerSerializer(serializers.ModelSerializer):
    """
    Сериализатор партнеров
    """

    class Meta:
        model = Partner
        exclude  = ["exhibitor",]
