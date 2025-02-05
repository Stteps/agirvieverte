from django.contrib.auth.forms import UserCreationForm

from app.users.models import BaseUser


class BaseUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = BaseUser
        fields = ["email"]
