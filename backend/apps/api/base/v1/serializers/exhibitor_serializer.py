from rest_framework import serializers

from ...models import Exhibitor


class ExhibitorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exhibitor
        fields  = "__all__"
