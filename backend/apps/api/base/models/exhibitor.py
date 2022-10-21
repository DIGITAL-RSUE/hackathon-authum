from django.db import models
from django.utils.translation import gettext_lazy as _

from ..enums import DisplayPrice, ImportSubstitution


class Exhibitor(models.Model):
    """
    Экспонент - участник выставки, выставляющий,
    демонстрирующий на ней что-либо
    """

    name = models.CharField(_("Название"), max_length=250)
    description = models.TextField(_("Описание"), blank=True, null=True,)
    about = models.TextField(_("О компании"), blank=True, null=True,)
    logo = models.ImageField(_("Логотип"), blank=True, null=True)
    main_picture = models.ImageField(_("Логотип"), blank=True, null=True)
    address = models.CharField(
        _("Адрес"), max_length=250, blank=True, null=True
    )
    legal_address = models.CharField(
        _("Юридический адрес"), max_length=250, blank=True, null=True
    )
    producer_address = models.CharField(
        _("Адрес производства"), max_length=250, blank=True, null=True
    )
    phone = models.CharField(
        _("Телефон"), max_length=25, blank=True, null=True
    )
    name_contact_person = models.CharField(
        _("ФМО контактного лица"), max_length=250, blank=True, null=True
    )
    inn = models.CharField(_("ИНН"), max_length=25, blank=True, null=True)
    display_price = models.IntegerField(
        verbose_name=_("Тип"),
        choices=DisplayPrice.choices,
        blank=True,
        null=True,
    )
    display_price_text = models.CharField(
        _("Цена (произвольный текст)"), max_length=50, blank=True, null=True
    )
    import_substitution = models.IntegerField(
        verbose_name=_("Импортозамещение"),
        choices=ImportSubstitution.choices,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Экспонент")
        verbose_name_plural = _("Экспоненты")


# Описание сущности “экспонент”:
# ID
# + наименование
# + описание
# мета-тэги: Title, meta-keywords, meta-description
# + блок “о компании”
# + логотип (поддержка файлов JPEG, PNG, SVG)
# + главное изображение (JPEG, PNG).
# категория на сайте: дропдаун
# + адрес сайта предприятия
# + номер телефона
# + ФИО контактного лица
# + ИНН предприятия
# + юридический адрес
# + адрес производства
# таблица локаций (ссылка на отдельный грид с CRUD)
# партнеры, клиенты (ссылка на отдельный грид с CRUD)
# отзывы партнеров (ссылка на отдельный грид с CRUD)
# каталог.
# Категории. Отдельный грид с CRUD
# товары, услуги. Отдельный грид с CRUD
# + Отображение цен на сайте. Значения:
# + “отображать”,
# + “не отображать”,
# + “Отображать произвольный текст”. Например это может быть текст “Цена договорная”, “Цена по запросу” и т.д. Текстовое поле, произвольный ввод.
# блок “портфолио”. Кейсы (ссылка на отдельный грид с CRUD)
# блок “импортозамещение”
# публикация. Отдельный грид с перечнем запросов на публикацию сущностей, их типом, наименованием сущности, статусом публикации, датой публикации, комментарием модератора.
# + шильд импортозамещения (отображать/не отображать)

# На странице редактирования экспонента группировать поля в отдельных табах, объединяя их в логические блоки. Например основные данные, данные учетной записи, локации, партнеры, отзывы, каталог и т.д.


# логин
# пароль
# email (может быть несколько)
# email для уведомлений от портала
