from apps.core.utils.model_mixin import (
    DatePublishedMixin,
    DateTimeCreatedMixin,
    IsPublishedMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(
    models.Model, IsPublishedMixin, DatePublishedMixin, DateTimeCreatedMixin
):
    """
    Категория
    """

    exhibitor = models.ForeignKey(
        "base.Exhibitor", verbose_name=_("Экспонент"), on_delete=models.CASCADE
    )
    name = models.CharField(_("Наименование"), max_length=150)
    parent = models.ForeignKey(
        "self",
        verbose_name=_("Родительская категория"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")


# Сущность “Категории”:
# ID
# + Название
# + тип связи (родительская/дочерняя)
# + Название связанной категории. Связь должна задаваться по ID, название резолвить по ID.
# + опубликован (да/нет/отклонено)
# + дата публикации (последняя)
