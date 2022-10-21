from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BaseConfig(AppConfig):
    """Default app config"""

    name = "apps.api.base"
    verbose_name = _("Base")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
