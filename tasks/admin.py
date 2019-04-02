from django.contrib import admin
from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'due_date', 'assigned_user',)
    list_filter = ('project', 'due_date', 'assigned_user')
