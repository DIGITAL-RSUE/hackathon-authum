from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated

class HasApiKeyOrIsAuthenticated(HasAPIKey):

    def has_permission(self, request, view):
        return super().has_permission(request, view) or bool(request.user and request.user.is_authenticated)
