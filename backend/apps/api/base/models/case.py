from apps.core.utils.model_mixin import DatePublishedMixin, IsPublishedMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..enums import ImportSubstitution, TypeContent


class Case(models.Model, IsPublishedMixin, DatePublishedMixin):
    """
    Сущность “Кейс”
    """

    exhibitor = models.ForeignKey(
        "base.Exhibitor", verbose_name=_("Экспонент"), on_delete=models.CASCADE
    )
    name = models.CharField(_("Название"), max_length=250)

    site_url = models.URLField(
        _("Ссылка на сайт партнера/заказчика"), blank=True, null=True
    )

    # Контент кейса
    type_content = models.IntegerField(
        verbose_name=_("Дата создания"), choices=TypeContent.choices,
    )
    html_content = models.TextField(_("HTML контент"), blank=True, null=True)
    video_content = models.URLField(_("Видео контент"), blank=True, null=True)

    import_substitution = models.IntegerField(
        verbose_name=_("Шильд импортозамещения"),
        choices=ImportSubstitution.choices,
        default=ImportSubstitution.NO,
    )

    class Meta:
        verbose_name = _("Кейс")
        verbose_name_plural = _("Кейсы")


# Сущность “Кейс”:
# ID
# + название кейса
# + тип контента: HTML/видео
# + HTML контент
# + ссылка на видеоконтент
# + опубликовано (да/нет/отклонено)
# + дата публикации. В поле отображается последняя дата публикации
# + шильд импортозамещения (отображать/не отображать)

