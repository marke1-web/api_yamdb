from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Review(models.Model):
    """Модель отзывов на произведения"""

    title = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Произведение",
    )
    text = models.CharField(max_length=200)
    author = models.ForeignKey(
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
