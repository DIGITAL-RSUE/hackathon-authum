from apps.core.utils.model_mixin import (
    DatePublishedMixin,
    DateTimeCreatedMixin,
    IsPublishedMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _


class Comment(
    models.Model, IsPublishedMixin, DatePublishedMixin, DateTimeCreatedMixin
):
    """
    Отзыв
    """

    exhibitor = models.ForeignKey(
        "base.Exhibitor", verbose_name=_("Экспонент"), on_delete=models.CASCADE
    )
    picture = models.ImageField(_("Изображение"), blank=True, null=True)
    name = models.CharField(_("ФИО"), max_length=150)
    company = models.CharField(
        _("Компания"), max_length=150, blank=True, null=True
    )
    text = models.TextField(_("Текст отзыва"))

    class Meta:
        verbose_name = _("Отзыв")
        verbose_name_plural = _("Отзывы")


# Сущность отзывы:
# ID
# + дата создания отзыва
# + текст отзыва
# оценка
# + ФИО и компания автора отзыва
# + изображение
# + опубликован (да/нет/отклонено)
# + дата публикации (последняя)
