from django.urls import path

from .views import Error403View, Error404View, Error500View

app_name = "errors"
urlpatterns = [
    path("500/", Error500View.as_view(), name="500"),
    path("403/", Error403View.as_view(), name="403"),
    path("404/", Error404View.as_view(), name="404"),
]

handler404 = Error403View.as_view()
handler500 = Error500View.as_view()
handler403 = Error404View.as_view()
