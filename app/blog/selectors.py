from .models import Article


def article_get(*, id: int) -> Article:
    return Article.objects.get(id=id)


def article_list_published():
    return Article.objects.all().order_by("-updated_at").filter(published=True)
