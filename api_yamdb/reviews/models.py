from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models



def validate_username(value):
    if not value or value == 'me':
        raise ValidationError(
            'Использовать никнейм "me" в качестве username запрещено'
        )
    return value


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    USER_ROLES = [
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (USER, 'Пользователь'),
    ]
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Имя пользователяяяяяяяяяяяяяяяяяяяяяяяяяя',
        validators=[UnicodeUsernameValidator(), validate_username],
    )
    email = models.EmailField(
        unique=True, verbose_name='Адрес электронной почты'
=======
class Review(models.Model):
    title = models.ForeignKey(on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(
        on_delete=models.CASCADE, related_name='reviews'

    )
    score = models.PositiveSmallIntegerField(
        verbose_name='Оценка',
        validators=[
            MinValueValidator(1, 'Оценка не может быть меньше 1'),
            MaxValueValidator(10, 'Оценка не может быть выше 10'),
        ],
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации', auto_now_add=True
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'], name='unique_author_title'
            )
        ]

    def __str__(self):
        return f'{self.title}, {self.score}, {self.author}'


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField(verbose_name='Текст комментария')
    author = models.ForeignKey(
        on_delete=models.CASCADE, related_name='comments'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата комментария', auto_now_add=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.author}, {self.pub_date}: {self.text}'
