from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""

    USER = "user"
    MODER = "moderator"
    ADMIN = "admin"
    ROLES = [
        (USER, "Аутентифицированный пользователь"),
        (MODER, "Модератор"),
        (ADMIN, "Администратор"),
    ]

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField("Почта", unique=True, max_length=254)
    role = models.CharField(
        verbose_name="Роль", max_length=250, choices=ROLES, default=USER
    )
    bio = models.TextField(
        "Биография",
        blank=True,
    )
    first_name = models.CharField("Имя", max_length=150, blank=True)
    last_name = models.CharField("Фамилия", max_length=150, blank=True)
    confirmation_code = models.CharField(
        max_length=150, blank=True, verbose_name="Код подтверждения"
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        constraints = [
            models.UniqueConstraint(
                fields=["username", "email"], name="unique_together"
            )
        ]

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_staff

    @property
    def is_moderator(self):
        return self.role == self.MODER

    def __str__(self):
        return self.username


class Category(models.Model):
    """Модель категории произведения"""

    name = models.CharField(
        blank=False,
        unique=True,
        max_length=32,
        verbose_name="Категория произведения",
    )
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Модель жанра произведения"""

    name = models.CharField(
        blank=False,
        unique=True,
        max_length=32,
        verbose_name="Жанр произведения",
    )
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


@admin.register(GenreTitle)
class GenreTitleAdmin(admin.ModelAdmin):
    """Класс настройки соответствия жанров и произведений."""

    list_display = (
        'pk',
        'genre',
        'title'
    )
    empty_value_display = 'значение отсутствует!'
    list_filter = ('genre',)
    list_per_page = LIST_PER_PAGE
    search_fields = ('title',)


class Title(models.Model):
    """Модель произведения"""

    name = models.CharField(
        blank=False, max_length=200, verbose_name="название произведения"
    )
    year = models.PositiveIntegerField(
        verbose_name="Год выпуска произведения", null=True
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="titles",
        verbose_name="Жанр",
    )

    class Meta:
        ordering = [
            "-id",
        ]

    def __str__(self):
        return self.name


class Review(models.Model):
    """Модель отзывов на произведения"""

    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Произведение",
    )
    text = models.CharField(max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Автор",
    )
    score = models.PositiveSmallIntegerField(
        validators=(
            MinValueValidator(1, message="Оценка не может быть меньше 1"),
            MaxValueValidator(10, message="Оценка не может быть больше 10"),
        ),
        verbose_name="Оценка",
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="Дата публикации"
    )

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Модель комментария"""

    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Комментарий",
    )
    text = models.CharField("Текст комментария", max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comment",
        verbose_name="Автор",
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="Дата публикации"
    )

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return self.text
