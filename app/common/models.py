from django.db import models
from django.db.models.query import F, Q
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(editable=False, db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    @property
    def created_at_prettified(self):
        return timezone.localtime(self.created_at).strftime("%Y/%m/%d %H:%M")

    @property
    def updated_at_prettified(self):
        return timezone.localtime(self.updated_at).strftime("%Y/%m/%d %H:%M")

    class Meta:
        abstract = True


class SimpleModel(models.Model):
    """
    This is a basic model used to illustrate a many-to-many relationship
    with RandomModel.
    """

    name = models.CharField(max_length=255, blank=True, null=True)


class RandomModel(BaseModel):
    """
    This is an example model, to be used as reference in the Styleguide,
    when discussing model validation via constraints.
    """

    start_date = models.DateField()
    end_date = models.DateField()

    simple_objects = models.ManyToManyField(SimpleModel, blank=True, related_name="random_objects")

    class Meta:
        constraints = [models.CheckConstraint(name="start_date_before_end_date", check=Q(start_date__lt=F("end_date")))]
