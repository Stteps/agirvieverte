import json

from constance import config
from django.shortcuts import render
from django.views import View

from .selectors import project_list


class IndexView(View):
    def get(self, request, *args, **kwargs):
        projects = [
            {
                "title": project.title,
                "picture": project.picture.url if project.picture else None,
            }
            for project in project_list()
        ]

        return render(
            request, "core/index.html", {"banner_path": config.LANDING_BANNER, "projects": json.dumps(projects)}
        )


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "core/about.html")
