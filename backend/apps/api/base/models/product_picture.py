from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductPicture(models.Model):
    """
    Изображение товара
    """

    product = models.ForeignKey(
        "base.Product",
        verbose_name=_("Товар"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="pictures",
    )
    picture = models.ImageField(_("Изображение"), blank=True, null=True)
    keywords = models.CharField(_("Ключевые слова"), max_length=150)

    class Meta:
        verbose_name = _("Изображение товара")
        verbose_name_plural = _("Изображения товара")


# Сущность “Категории”:
# ID
# + Название
# + тип связи (родительская/дочерняя)
# + Название связанной категории. Связь должна задаваться по ID, название резолвить по ID.
# + опубликован (да/нет/отклонено)
# + дата публикации (последняя)
