from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderNumberMixin:
    """
    add order_number field
    """

    order_number = models.IntegerField(
        verbose_name=_("Порядковый номер"), blank=True, null=True,
    )


class DateTimeCreatedMixin:
    """
    add date_time_created field
    """

    date_time_created = models.DateTimeField(
        verbose_name=_("Дата создания"), auto_now_add=True
    )


class DatePublishedMixin:
    """
    add date_published field
    """

    date_published = models.DateField(
        verbose_name=_("Дата публикации"), blank=True, null=True
    )


class IsPublishedMixin:
    """
    add is_published field
    """

    class IsPublished(models.IntegerChoices):
        NO = 0, _("Нет")
        YES = 1, _("Да")
        CANCELED = 2, _("Отменено")

    is_published = models.IntegerField(
        verbose_name=_("Является опубликованным"),
        choices=IsPublished.choices,
        default=IsPublished.NO,
    )


class DisplayMixin:
    """
    add display field
    """

    class Display(models.IntegerChoices):
        NO = 0, _("Нет")
        YES = 1, _("Да")

    display = models.IntegerField(
        verbose_name=_("Отображение"),
        choices=Display.choices,
        default=Display.NO,
    )
