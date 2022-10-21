from django.db import models
from django.utils.translation import gettext_lazy as _


class Brand(models.Model):
    """
    Бренд
    """

    name = models.CharField(_("Наименование"), max_length=150)

    class Meta:
        verbose_name = _("Бренд")
        verbose_name_plural = _("Бренды")
