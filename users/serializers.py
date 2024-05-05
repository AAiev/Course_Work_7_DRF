from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from users.models import User



class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели пользователя
    """

    password = serializers.CharField(
        max_length=68, min_length=3)

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.
        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

    class Meta:
        model = User
        fields = ('id', 'email', 'chat_id', 'password',)
