from djoser.serializers import UserCreateSerializer as CustomUserCreateSerializer


class UserCreateSerializer(CustomUserCreateSerializer):
    class Meta(CustomUserCreateSerializer.Meta):
        fields = [
            "id", "username", "password", "email", "first_name", "last_name"
        ]
