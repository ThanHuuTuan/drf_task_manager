import pydash
from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        model = get_user_model()
        instance = model(**validated_data)
        user = pydash.get(self, 'context.request.user')
        if not (user and user.is_superuser):
            instance.is_superuser = False
        # Hash the user's password.
        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'role')
