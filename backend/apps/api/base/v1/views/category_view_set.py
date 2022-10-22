from rest_framework import status, viewsets

from ...models import Category
from ..serializers import CategorySerializer

# from rest_framework.decorators import action
# from rest_framework.response import Response


# from myapp.serializers import UserSerializer, PasswordSerializer


class ModeratorCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_url_kwarg = "id"




class ExhibitorCategoryViewSet(ModeratorCategoryViewSet):

    def get_object(self):
        self.kwargs[self.lookup_url_kwarg or self.lookup_field] = self.request.user.id
        return super().get_object()
