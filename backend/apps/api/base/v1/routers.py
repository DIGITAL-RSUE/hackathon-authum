from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ExhibitorCategoryViewSet, ModeratorCategoryViewSet

app_name = "base"

router = DefaultRouter()

router.register(r'moderator/category/<int:exhibitor_id>', ModeratorCategoryViewSet, basename='m-category')

router.register(r'exhibitor/category', ExhibitorCategoryViewSet, basename='e-category')

urlpatterns = [
    # EXHIBITOR URLS
    # path("category/", ModeratorCategoryViewSet.as_view({'get':'list'}), name="category"),
    # path("category/", ModeratorCategoryViewSet.as_view({'post':'create'}), name="category"),
    # path("location/", .as_view(), name=""),
    # path("comment/", .as_view(), name=""),
    # path("product/", .as_view(), name=""),
    # path("partner/", .as_view(), name=""),
    # path("case/", .as_view(), name=""),

    # MODETATOR URLS
    # Exhibitor profile:
    # path("exhibitor/", .as_view(), name=""),
    # path("category/", .as_view(), name=""),
    # path("location/", .as_view(), name=""),
    # path("comment/", .as_view(), name=""),
    # path("product/", .as_view(), name=""),
    # path("partner/", .as_view(), name=""),
    # path("case/", .as_view(), name=""),
    # Other:
    # path("brand/", .as_view(), name=""),
    # path("producer/", .as_view(), name=""),
    # path("type-cooperation/", .as_view(), name=""),

]

urlpatterns += router.urls
