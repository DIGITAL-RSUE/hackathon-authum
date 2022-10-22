from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "base"


router = DefaultRouter()

# EXHIBITOR URLS REGISTER
router.register(r'exhibitor/category', views.ExhibitorCategoryViewSet)
router.register(r'exhibitor/case', views.ExhibitorCaseViewSet)
router.register(r'exhibitor/comment', views.ExhibitorCommentViewSet)
router.register(r'exhibitor/location', views.ExhibitorLocationViewSet)
router.register(r'exhibitor/partner', views.ExhibitorPartnerViewSet)
router.register(r'exhibitor/product', views.ExhibitorProductViewSet)

# MODETATOR URLS REGISTER
router.register(r'moderator/category/(?P<exhibitor_id>\d+)', views.ModeratorCategoryViewSet)
router.register(r'moderator/case/(?P<exhibitor_id>\d+)', views.ModeratorCaseViewSet)
router.register(r'moderator/comment/(?P<exhibitor_id>\d+)', views.ModeratorCommentViewSet)
router.register(r'moderator/location/(?P<exhibitor_id>\d+)', views.ModeratorLocationViewSet)
router.register(r'moderator/partner/(?P<exhibitor_id>\d+)', views.ModeratorPartnerViewSet)
router.register(r'moderator/product/(?P<exhibitor_id>\d+)', views.ModeratorProductViewSet)
router.register(r'moderator/exhibitor', views.ModeratorExhibitorViewSet)

urlpatterns = []

urlpatterns += router.urls
