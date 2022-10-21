DEFAULT_APPS = [
    "admin_interface",
    "colorfield",
    "extra_settings",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "import_export",
    "corsheaders",
    "modeltranslation",
    "widget_tweaks",
    "rest_framework",
    "drf_yasg",
    "django_cleanup.apps.CleanupConfig",
    "etc",
    "service_objects",
    "ckeditor",
    "ckeditor_uploader",
]

PROJECT_APPS = [
    "apps.core.utils",
    "apps.core.main",
    "apps.core.api",
    "apps.api.auth",
    "apps.api.base",
]

DEVELOPER_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
    "django_extensions",
    "debug_toolbar",
]

PRODUCTION_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
]
