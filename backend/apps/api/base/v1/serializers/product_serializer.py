from rest_framework import serializers

from ...models import Product, ProductPicture


class ProductPictureSerializer(serializers.ModelSerializer):
    """
    Сериализатор картинки товарара
    """

    class Meta:
        model = ProductPicture
        fields  = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор экспонента
    """

    pictures = ProductPictureSerializer(many=True)

    class Meta:
        model = Product
        exclude  = ["exhibitor",]
