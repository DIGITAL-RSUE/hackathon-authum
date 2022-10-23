from rest_framework import serializers

from ...models import Category


class SubCategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор подкатегорий
    """

    class Meta:
        model = Category
        exclude  = ["exhibitor",]


class CategoryNestedSerializer(serializers.ModelSerializer):
    """
    Сериализатор Сериализатор
    вложенных категорий
    """

    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        exclude  = ["exhibitor",]


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор категорий
    """

    class Meta:
        model = Category
        exclude  = ["exhibitor",]
