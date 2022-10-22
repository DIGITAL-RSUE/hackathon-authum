from rest_framework import serializers

from ...models import Category


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude  = ["exhibitor",]

class CategoryNestedSerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)
    class Meta:
        model = Category
        exclude  = ["exhibitor",]

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)
    class Meta:
        model = Category
        exclude  = ["exhibitor",]
