from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    fields = (
        "title",
        "slug",
        "picture",
        "content",
        "published",
        "updated_at",
        "created_at",
    )
    list_display = ("title", "published", "created_at", "updated_at")
    list_filter = ("published",)

    readonly_fields = (
        "slug",
        "updated_at",
        "created_at",
    )
