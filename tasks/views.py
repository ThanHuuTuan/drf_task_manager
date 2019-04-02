from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework import viewsets
from system.permissions import ManagerOrAdminOrReadOnly
from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (ManagerOrAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['due_date', ]


class UserTaskView(TaskView):
    def get_queryset(self):
        user_id = self.kwargs['user_pk']
        return self.queryset.filter(assigned_user_id=user_id)



