from rest_framework import permissions


class IsOwnerOrStaffOrAdmin(permissions.IsAuthenticated):
  def has_object_permission(self, request, view, obj):
    return request.user == obj
