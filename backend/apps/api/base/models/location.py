from apps.core.utils.model_mixin import DisplayMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class Location(models.Model, DisplayMixin):
    """
    Локация
    """

    exhibitor = models.ForeignKey(
        "base.Exhibitor", verbose_name=_("Экспонент"), on_delete=models.CASCADE
    )
    name = models.CharField(_("Наименование"), max_length=150)
    type_cooperation = models.ForeignKey(
        "base.TypeCooperation",
        verbose_name=_("Тип сотрудничества"),
        blank=True,
        null=True,
    )
    site_url = models.URLField(
        _("Ссылка на сайт партнера/заказчика"), blank=True, null=True
    )
    address = models.CharField(
        _("Адрес"), max_length=150, blank=True, null=True
    )

    class Meta:
        verbose_name = _("Локация")
        verbose_name_plural = _("Локации")


# Сущность “локации”:
# ID
# + адрес
# GPS - координаты
# + наименование
# + тип сотрудничества (головной офис, филиал, дилер, партнер и т.д.). Текстовое поле, свободный ввод
# + ссылка на сайт партнера
# + статус (включен/отключен). Отключенные объекты не должны отображаться на фронте.

# Грид локаций должен содержать чекбокс выбора записей, выбора/отмены выбора всех записей, масс-экшены включения/отключения.
