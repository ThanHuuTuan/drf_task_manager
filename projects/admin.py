from django.contrib import admin
from projects.models import Project
from tasks.models import Task


class TaskInline(admin.TabularInline):
    model = Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [TaskInline, ]
