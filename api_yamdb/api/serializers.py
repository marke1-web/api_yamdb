from rest_framework.serializers import (
    CharField,
    ModelSerializer,
)

from reviews.models import (
    User,
)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )


class ProfileSerializer(UserSerializer):
    role = CharField(read_only=True)


class SignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class TokenSerializer(ModelSerializer):
    username = CharField()
    confirmation_code = CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')
