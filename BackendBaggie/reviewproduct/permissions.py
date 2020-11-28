from rest_framework.permissions import BasePermission, SAFE_METHODS


class CanCreatePermissionforCustomer(BasePermission):
    """Client admins should be able to edit property they own"""

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True

        if user.role == 'customer' and user.is_authenticated:
            return True
        else:
            return False


class CanUpdateDeletePermissionforVendor(BasePermission):
    """Client admins should be able to edit property they own"""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if user.role == 'vendor' and user.is_authenticated:
            return True
        else:
            return False
