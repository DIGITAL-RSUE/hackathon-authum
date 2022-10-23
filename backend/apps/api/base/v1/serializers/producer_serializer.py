from rest_framework import serializers

from ...models import Producer


class ProducerSerializer(serializers.ModelSerializer):
    """
    Сериализатор производителей
    """

    class Meta:
        model = Producer
        exclude  = ["exhibitor",]
