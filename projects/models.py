from django.db import models
from users.models import User


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    users = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.title
