from django.db import models
from django.utils.translation import gettext_lazy as _


class TypePurchase(models.IntegerChoices):
    """
    Возможность приобретения
    """

    WHOLESALE = 0, _("Опт")
    RETAIL = 1, _("Розница")
    BOTH = 1, _("Оба варианта")
