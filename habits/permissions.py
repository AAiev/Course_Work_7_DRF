from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Кастомный пермишен для проверк, является ли пользователь владельцем запрашиваемых привычек
    """
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
