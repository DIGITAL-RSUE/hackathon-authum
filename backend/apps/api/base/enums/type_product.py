from django.db import models
from django.utils.translation import gettext_lazy as _


class TypeProduct(models.IntegerChoices):
    """
    Перечисление типов товара
    """

    GOODS = 0, _("Товар")
    SERVICE = 1, _("Услуга")
