from rest_framework import status, viewsets
from rest_framework.decorators import action

from ...models import Comment
from ..serializers import CommentSerializer



class ExhibitorCommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()



class ModeratorCommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
