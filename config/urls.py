import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.urls import include, path

urlpatterns = [
    path("ws/", include("app.core.routing", namespace="core_ws")),
    path("auth/", include("app.authentication.urls", namespace="authentication")),
]

urlpatterns += i18n_patterns(
    path(_("admin/"), admin.site.urls, name="admin"),
    path("api/", include("app.api.urls", namespace="api")),
    path("", include("app.core.urls", namespace="core")),
    path("blog/", include("app.blog.urls", namespace="blog")),
    path("", include("app.errors.urls", namespace="errors")),
    path("users/", include("app.users.urls", namespace="users")),
)

if os.environ.get("DJANGO_SETTINGS_MODULE") == "config.django.base":
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from config.settings.debug_toolbar.setup import DebugToolbarSetup  # noqa

urlpatterns = DebugToolbarSetup.do_urls(urlpatterns)
