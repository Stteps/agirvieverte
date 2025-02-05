from django.conf import settings
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect


class PermissionRequiredMixin(PermissionRequiredMixin):
    permission_required = "users.is_allowed"

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return HttpResponseRedirect(settings.REQUEST_DEMO_ACCESS_URL)
        return super().dispatch(request, *args, **kwargs)
