from rest_framework import permissions

class IsOwnerGetbyUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user==obj.user