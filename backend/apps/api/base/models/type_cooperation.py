from django.db import models
from django.utils.translation import gettext_lazy as _


class TypeCooperation(models.Model):
    """
    Тип сотрудничества
    """

    name = models.CharField(_("Наименование"), max_length=150)

    class Meta:
        verbose_name = _("Тип сотрудничества")
        verbose_name_plural = _("Типы сотрудничества")
