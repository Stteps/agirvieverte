from django.core.validators import FileExtensionValidator
from django.db import models

from app.common.models import BaseModel


class Project(BaseModel):
    ALLOWED_IMAGE_EXTENSIONS = ["png", "jpg", "jpeg", "gif", "ico"]

    title = models.CharField(max_length=128)

    picture = models.ImageField(
        help_text=f"Upload picture with format in {ALLOWED_IMAGE_EXTENSIONS}",
        upload_to="projects",
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=ALLOWED_IMAGE_EXTENSIONS, message="Wrong picture format"),
        ],
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
