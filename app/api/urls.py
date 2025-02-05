from django.urls import include, path

app_name = "api"
urlpatterns = [
    path("", include("app.core.endpoints", namespace="core")),
    path("users/", include("app.users.endpoints", namespace="users")),
]
