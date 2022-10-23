from rest_framework import serializers

from ...models import Exhibitor


class ExhibitorSerializer(serializers.ModelSerializer):
    """
    Сериализатор экспонента
    """

    class Meta:
        model = Exhibitor
        fields  = "__all__"
