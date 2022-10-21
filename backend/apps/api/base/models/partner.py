from apps.core.utils.model_mixin import (
    DatePublishedMixin,
    IsPublishedMixin,
    OrderNumberMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _


class Partner(models.Model, IsPublishedMixin, OrderNumberMixin):
    """
    Партнер
    """

    exhibitor = models.ForeignKey(
        "base.Exhibitor", verbose_name=_("Экспонент"), on_delete=models.CASCADE
    )
    logo = models.ImageField(_("Логотип"), blank=True, null=True)
    name = models.CharField(_("Наименование"), max_length=250)

    class Meta:
        verbose_name = _("Партнер")
        verbose_name_plural = _("Партнеры")


# Сущность “Партнер”:
# ID
# + наименование
# + логотип/изображение
# + порядок отображения. Определяет очередность вывода в блоке
# + опубликовано. Да, нет, отклонено
