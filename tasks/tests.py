from django.test import TestCase

# Create your tests here.
from django.utils import timezone

from projects.models import Project
from tasks.models import Task
from users.models import User


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='test_name', email='email@mail.com', password='123qweasd')
        project = Project.objects.create(title='Writing tests')
        Task.objects.create(title='Create test', due_date=timezone.now(), project=project, assigned_user=user)

    def test_task_description_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Description')

    def test_task_title_max_length(self):
        task = Task.objects.get(id=1)
        max_length = task._meta.get_field('title').max_length
        self.assertEquals(max_length, 255)

