from django.contrib import admin

from .models import Category, Comment, Genre, GenreTitle, Review, Title, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Класс настройки раздела пользователей."""

    list_display = (
        "id",
        "username",
        "email",
        "role",
        "bio",
        "first_name",
        "last_name",
        "confirmation_code",
    )
    search_fields = ("username", "role")
    list_filter = ("username",)
    empty_value_display = "-пусто-"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс настройки раздела категорий."""

    list_display = (
        "id",
        "name",
        "slug",
    )
    search_fields = ("name",)
    list_filter = ("name",)
    empty_value_display = "-пусто-"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Класс настройки раздела жанров."""

    list_display = (
        "id",
        "name",
        "slug",
    )
    search_fields = ("name",)
    list_filter = ("name",)
    empty_value_display = "-пусто-"


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    """Класс настройки раздела произведений."""

    list_display = (
        "id",
        "name",
        "year",
        "category",
    )
    search_fields = (
        "name",
        "year",
    )
    list_filter = (
        "name",
        "year",
    )
    empty_value_display = "-пусто-"


@admin.register(GenreTitle)
class GenreTitleAdmin(admin.ModelAdmin):
    """Класс настройки соответствия жанров и произведений."""

    list_display = ("id", "title", "genre")
    search_fields = ("title",)
    list_filter = ("genre",)
    empty_value_display = "-пусто-"


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
