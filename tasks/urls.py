from django.conf.urls import url, include
from rest_framework import routers
from tasks.views import TaskView, UserTaskView

router = routers.DefaultRouter()
router.register(r'users/(?P<user_pk>\d+)/tasks', UserTaskView, base_name='user_task')  # get tasks by assigned user id
router.register('tasks', TaskView)  # CRUD for tasks

urlpatterns = [
    url('', include(router.urls)),
]
