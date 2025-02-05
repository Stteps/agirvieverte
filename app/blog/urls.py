from django.urls import path

from .views import ArticleView, IndexView

app_name = "blog"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<str:slug>/", ArticleView.as_view(), name="article"),
]
