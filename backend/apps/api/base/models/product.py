from apps.core.utils.model_mixin import DatePublishedMixin, IsPublishedMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..enums import (
    DeliveryMethod,
    ImportSubstitution,
    PaymentMethod,
    TypeProduct,
    TypePurchase,
)


class Product(
    models.Model, IsPublishedMixin, DatePublishedMixin,
):
    """
    Товар
    """

    exhibitor = models.ForeignKey(
        "base.Exhibitor", verbose_name=_("Экспонент"), on_delete=models.CASCADE
    )
    name = models.CharField(_("Название"), max_length=250)
    price = models.FloatField(_("Цена"), blank=True, null=True,)
    description = models.TextField(_("Описание"), blank=True, null=True,)
    analogues = models.TextField(_("Аналоги"), blank=True, null=True,)
    type_product = models.IntegerField(
        verbose_name=_("Тип"),
        choices=TypeProduct.choices,
        blank=True,
        null=True,
    )
    import_substitution = models.IntegerField(
        verbose_name=_("Импортозамещение"),
        choices=ImportSubstitution.choices,
        blank=True,
        null=True,
    )
    type_purchase = models.IntegerField(
        verbose_name=_("Возможность приобретения"),
        choices=TypePurchase.choices,
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        "base.Category",
        verbose_name=_("Категория"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    delivery_method = models.IntegerField(
        verbose_name=_("Способ доставки"), choices=DeliveryMethod.choices,
    )
    payment_method = models.IntegerField(
        verbose_name=_("Способ оплаты"), choices=PaymentMethod.choices,
    )
    minimum_batch = models.IntegerField(
        _("Минимальная партия"), default=1, blank=True, null=True,
    )
    producer = models.ForeignKey(
        "base.Producer",
        verbose_name=_("Производитель"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    brand = models.ForeignKey(
        "base.Brand",
        verbose_name=_("Бренд"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    video = models.URLField(_("Видео контент"), blank=True, null=True)

    class Meta:
        verbose_name = _("Товар")
        verbose_name_plural = _("Товары")


# Сущность “Товар”:
# ID
# + тип (товар/услуга)
# + производитель
# + торговая марка/бренд
# + название
# + изображение (может быть несколько)
# + видео
# + описание
# + цена
# мета-тэги
# + категория
# + возможность приобретения (опт/розница, оба варианта)
# + минимальная партия
# + способ оплаты
# + способ доставки
# соответствие стандартам
# + аналоги (произвольный текст)
# + опубликовано (да/нет/отклонено)
# + дата публикации. В поле отображается последняя дата публикации
# + шильд импортозамещения (отображать/не отображать)
