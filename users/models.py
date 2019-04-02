from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = (
        ('manager', 'Manager'),
        ('developer', 'Developer'),
    )

    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(verbose_name='email', unique=True)
    role = models.CharField(max_length=255, choices=ROLES, default='developer')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
