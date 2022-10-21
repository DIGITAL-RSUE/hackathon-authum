from django.db import models
from django.utils.translation import gettext_lazy as _


class TypeContent(models.IntegerChoices):
    """
    Перечисление типов контента
    """

    HTML = 0, _("HTML")
    VIDEO = 1, _("Видео")
