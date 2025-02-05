import json

from django.shortcuts import render
from django.views import View

from .selectors import article_get, article_list_published


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = [
            {
                "title": project.title,
                "picture": project.picture.url if project.picture else json.dumps(None),
                "url": project.url,
            }
            for project in article_list_published()
        ]

        return render(request, "blog/index.html", {"articles": articles})


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = article_get(slug=kwargs["slug"])
        return render(request, "blog/article.html", {"article": article})
