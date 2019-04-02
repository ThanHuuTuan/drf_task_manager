import pydash
from django.contrib.auth import get_user_model
from rest_framework import serializers

from projects.models import Project
from users.models import User
from users.serializers import UserInfoSerializer


class ProjectSerializer(serializers.ModelSerializer):
    users = UserInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

    def add_users(self, instance, users_ids):
        for user_id in users_ids:
            instance.users.add(user_id)
        instance.save()
        return instance

    def create(self, validated_data):
        users_ids = pydash.get(self, 'context.request.data.users')
        instance = super().create(validated_data)
        return self.add_users(instance, users_ids=users_ids)

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.users.clear()
        users_ids = pydash.get(self, 'context.request.data.users')
        return self.add_users(instance, users_ids=users_ids)
