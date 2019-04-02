from django.contrib import admin
from users.models import User

class ProjectInline(admin.TabularInline):
    model = User.projects.through


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [ProjectInline, ]
