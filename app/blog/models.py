from django.core.validators import FileExtensionValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from app.common.models import BaseModel


class Article(BaseModel):
    ALLOWED_IMAGE_EXTENSIONS = ["png", "jpg", "jpeg"]

    title = models.CharField(max_length=255)  # Title of the article
    slug = models.SlugField(null=True, blank=True, unique=True)  # Unique reference name for the URL
    picture = models.ImageField(
        help_text=f"Upload picture with format in {ALLOWED_IMAGE_EXTENSIONS}",
        upload_to="articles",
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=ALLOWED_IMAGE_EXTENSIONS, message="Wrong picture format"),
        ],
    )
    content = models.TextField()  # Content of the article

    published = models.BooleanField(default=True)  # Publication status (displayed or not on the website)

    @property
    def url(self):  # Returns the absolute URL of the article
        return reverse("blog:article", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
