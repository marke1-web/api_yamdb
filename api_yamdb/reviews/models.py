from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
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
    )
    role = models.CharField(
        max_length=30, choices=USER_ROLES, default=USER, verbose_name='Роль'
    )
    bio = models.TextField(blank=True, verbose_name='Биография')
    confirmation_code = models.CharField(
        verbose_name='Код подтверждения', max_length=36, blank=True, null=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR
