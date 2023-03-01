from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Класс разрешений объект меняет только автор"""
    def has_object_permission(self, request, view, obj):
        """Метод проверки доступа на уровне объекта"""
        if request.method in permissions.SAFE_METHODS:

            return True

        return obj.author == request.user
