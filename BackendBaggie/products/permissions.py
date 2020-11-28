from rest_framework.permissions import BasePermission, SAFE_METHODS


class CanEditPermissionForProducts(BasePermission):
    """Client admins should be able to edit property they own"""

    def has_permission(self, request, view):
        #print('user hi :', request.user.id)
        user = request.user
        if request.method in SAFE_METHODS:
            return True
        if user.role == 'vendor' and user.is_authenticated:
            return True
        else:
            return False


# class IsOwner(permissions.BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#         return obj.owner == request.user
