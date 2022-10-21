from django.db import models
from django.utils.translation import gettext_lazy as _


class PaymentMethod(models.IntegerChoices):
    """
    Перечисление способ оплаты
    """

    HTML = 0, _("HTML")
    VIDEO = 1, _("Видео")
