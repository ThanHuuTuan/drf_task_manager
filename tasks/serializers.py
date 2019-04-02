from rest_framework import serializers

from projects.serializers import ProjectSerializer
from tasks.models import Task
from users.serializers import UserInfoSerializer


class TaskSerializer(serializers.ModelSerializer):
    project_id = serializers.IntegerField(write_only=True,)
    assigned_user_id = serializers.IntegerField(write_only=True,)

    project = ProjectSerializer(read_only=True)
    assigned_user = UserInfoSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
