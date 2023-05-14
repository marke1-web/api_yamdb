from django.contrib import admin

from .models import Comment, Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Класс настройки раздела отзывов."""

    list_display = (
        "id",
        "title",
        "text",
        "author",
        "score",
        "pub_date",
    )
    search_fields = (
        "author",
        "title",
    )
    list_filter = (
        "author",
        "pub_date",
    )
    empty_value_display = "-пусто-"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Класс настройки раздела комментариев."""

    list_display = (
        "id",
        "review",
        "text",
        "author",
        "pub_date",
    )
    search_fields = (
        "author",
        "review",
    )
    list_filter = (
        "author",
        "pub_date",
    )
    empty_value_display = "-пусто-"
