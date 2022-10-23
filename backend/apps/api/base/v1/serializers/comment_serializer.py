from rest_framework import serializers

from ...models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор комментариев
    """

    class Meta:
        model = Comment
        exclude  = ["exhibitor",]
