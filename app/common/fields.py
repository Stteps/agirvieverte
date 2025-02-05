from django.core.exceptions import ValidationError
from django.forms import Field


class SpanField(Field):
    empty_values = [""]

    def to_python(self, value):
        try:
            value = eval(value)
        except Exception:
            raise ValidationError("Invalid value")

        if not isinstance(value, (list, tuple)) or len(value) != 2:
            raise ValidationError("Value must be a tuple or list of length 2")
        if not all(isinstance(v, int) and v >= 0 for v in value):
            raise ValidationError("Values must be positive integers")
        if value[0] > value[1]:
            raise ValidationError("First value must be less than or equal to the second")

        return value


class SpanArrayField(Field):
    empty_values = [""]

    def to_python(self, value):
        try:
            value = eval(value)
        except Exception:
            raise ValidationError("Invalid value")

        if not isinstance(value, list):
            raise ValidationError("Value must be a list.")
        for span in value:
            if not isinstance(span, (list, tuple)) or len(span) != 2:
                raise ValidationError("Each value in the list must be a tuple or list of length 2.")
            if not all(isinstance(v, int) and v >= 0 for v in span):
                raise ValidationError("Values in each tuple must be positive integers.")
            if span[0] > span[1]:
                raise ValidationError("First value in each tuple must be less than or equal to the second.")

        return value
