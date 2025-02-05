from django.db import models

from app.common.models import BaseModel


class Email(BaseModel):
    class Status(models.TextChoices):
        READY = "READY", "Ready"
        SENDING = "SENDING", "Sending"
        SENT = "SENT", "Sent"
        FAILED = "FAILED", "Failed"

    status = models.CharField(max_length=255, db_index=True, choices=Status.choices, default=Status.READY)

    to = models.EmailField()
    subject = models.CharField(max_length=255)

    html = models.TextField(blank=True)
    plain_text = models.TextField(blank=True)

    sent_at = models.DateTimeField(blank=True, null=True)
