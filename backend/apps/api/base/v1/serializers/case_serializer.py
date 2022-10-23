from rest_framework import serializers

from ...models import Case


class CaseSerializer(serializers.ModelSerializer):
    """
    Сериализатор Кейса
    """

    class Meta:
        model = Case
        exclude  = ["exhibitor",]
