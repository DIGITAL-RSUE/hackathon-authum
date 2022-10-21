from django.db import models
from django.utils.translation import gettext_lazy as _


class ImportSubstitution(models.IntegerChoices):
    """
    Импортозамещение
    """

    NO = 0, _("Нет")
    YES = 1, _("Да")
