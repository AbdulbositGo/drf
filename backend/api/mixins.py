from rest_framework import permissions

from .permissons import IsStaffEditorPermission


class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] 