from django.core.validators import FileExtensionValidator


CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"

CONSTANCE_ADDITIONAL_FIELDS = {
    "image_field": [
        "django.forms.ImageField",
        {"validators": [FileExtensionValidator(allowed_extensions=["png", "jpg"])]},
    ],
}

CONSTANCE_CONFIG = {
    "LANDING_BANNER": ("none.png", "Cover Picture", "image_field"),
}

CONSTANCE_CONFIG_FIELDSETS = {
    "Landing": ("LANDING_BANNER",),
}
