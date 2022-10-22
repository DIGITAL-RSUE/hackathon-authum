"""Rest framework settings"""

DATE_INPUT_FORMATS = [
    ("%d-%m-%Y"),
    ("%d.%m.%Y"),
    ("%d/%m/%Y"),
    "iso-8601",
]


REST_FRAMEWORK = {
    # "DEFAULT_PERMISSION_CLASSES": (
    #     "apps.core.api.permissions.HasApiKeyOrIsAuthenticated",
    # ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    # ),
    "DEFAULT_RENDERER_CLASSES": (
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
        "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": (
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
    ),
    "DATE_FORMAT": "%d.%m.%Y",
    "DATE_INPUT_FORMATS": DATE_INPUT_FORMATS,
    "DATETIME_FORMAT": "%d.%m.%Y %H:%M",
}

CORS_ALLOW_ALL_ORIGINS = True
