from django.db import models
from django.utils.translation import gettext_lazy as _


class DisplayPrice(models.IntegerChoices):
    """
    Перечисление
    """

    NO = 0, _("Нет")
    YES = 1, _("Да")
    TEXT = 1, _("Отображать текст")
