from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an objects to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS or
            request.user == obj.owner
        )
