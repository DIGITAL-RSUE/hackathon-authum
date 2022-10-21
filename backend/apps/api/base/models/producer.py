from django.db import models
from django.utils.translation import gettext_lazy as _


class Producer(models.Model):
    """
    Производитель
    """

    name = models.CharField(_("Наименование"), max_length=150)

    class Meta:
        verbose_name = _("Производитель")
        verbose_name_plural = _("Производители")
