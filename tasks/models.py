from django.db import models


# Create your models here.
from projects.models import Project
from users.models import User


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_tasks')
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tasks')

    def __str__(self):
        return self.title
