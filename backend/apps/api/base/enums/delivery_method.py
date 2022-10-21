from django.db import models
from django.utils.translation import gettext_lazy as _


class DeliveryMethod(models.IntegerChoices):
    """
    Перечисление методов доставки
    """

    HTML = 0, _("HTML")
    VIDEO = 1, _("Видео")
