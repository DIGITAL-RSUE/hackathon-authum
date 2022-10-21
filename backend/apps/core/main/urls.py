from django.urls import include, path, re_path

from .views import MainRedirectView

urlpatterns = [
    path("", MainRedirectView.as_view()),
    path("api/", include("apps.core.api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    re_path(r"^ckeditor/", include("ckeditor_uploader.urls")),
]
