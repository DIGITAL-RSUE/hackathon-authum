"""Rest framework settings"""

import os
from datetime import timedelta

from config.settings.base import env

from .paths import KEYS_DIR

DATE_INPUT_FORMATS = [
    ("%d-%m-%Y"),
    ("%d.%m.%Y"),
    ("%d/%m/%Y"),
    "iso-8601",
]

REST_FRAMEWORK = {
    "DATETIME_INPUT_FORMATS": DATE_INPUT_FORMATS,
    "DATE_FORMAT": "%d/%m/%Y",
    "DATETIME_FORMAT": "%d/%m/%Y %H:%M",
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_RENDERER_CLASSES": (
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
        "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
        # Any other renders
    ),
    "DEFAULT_PARSER_CLASSES": (
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
        # Any other parsers
    ),
}

CORS_ORIGIN_ALLOW_ALL = True

JWT_ALGORITHM = env("JWT_ALGORITHM", default="HS256")

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": JWT_ALGORITHM,
    "AUTH_COOKIE": "auth_token",
    "AUTH_COOKIE_SECURE": False,
}

if JWT_ALGORITHM in ["RS256", "RS384", "RS512"]:
    PUBLIC_KEY_NAME = env("JWT_PUBLIC_FILE", default="jwt.crt")
    PRIVATE_KEY_NAME = env("JWT_PRIVATE_FILE", default="jwt.key")
    PUBLIC_KEY_PATH = os.path.join(KEYS_DIR, PUBLIC_KEY_NAME)
    PRIVATE_KEY_PATH = os.path.join(KEYS_DIR, PRIVATE_KEY_NAME)
    SIMPLE_JWT["SIGNING_KEY"] = open(PRIVATE_KEY_PATH, "rb").read()
    SIMPLE_JWT["VERIFYING_KEY"] = open(PUBLIC_KEY_PATH, "rb").read()
