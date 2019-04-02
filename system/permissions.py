from rest_framework import permissions
from rest_framework.exceptions import NotFound


class ManagerOrAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow developers or admin or ReadOnly.
    """

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser or request.user.role == 'manager'

