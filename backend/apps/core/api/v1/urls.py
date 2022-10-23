from django.urls import include, path

app_name = "v1"

urlpatterns = [
    path("base/", include("apps.api.base.v1")),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
]
