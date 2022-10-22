from rest_framework import status, viewsets
from rest_framework.decorators import action

from ...models import Category
from ..serializers import CategoryNestedSerializer, CategorySerializer

# from rest_framework.decorators import action
# from rest_framework.response import Response


# from myapp.serializers import UserSerializer, PasswordSerializer


class ExhibitorCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()



class ModeratorCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    # @action(url_path="<int:exhibitor_id>", detail=False, url_name="moderator")
    # def category_list_moderator(self):
    #     queryset = self.filter_queryset(self.get_queryset().filter(exhibitor__id=self.kwargs["exhibitor_id"]))

    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # @action(url_path="<int:exhibitor_id>", detail=True, url_name="moderator")
    # def category_retrive_moderator(self):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)


# class ExhibitorCategoryViewSet(ModeratorCategoryViewSet):

#     def get_object(self):
#         self.kwargs[self.lookup_url_kwarg or self.lookup_field] = self.request.user.id
#         return super().get_object()
