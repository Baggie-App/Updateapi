# from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class CanEditProperty(BasePermission):
    message = 'Adding customers not allowed.'
    """Client admins should be able to edit property they own"""

    def has_permission(self, request, view):
        #print('user hi :', request.user.id)
        user = request.user
        if request.method in SAFE_METHODS:
            return True
        # role = request.data.get('role')
        # print("role",role)
        if user.role == 'customers':
            return False
        if user.role == 'superuser' and user.is_authenticated:
            return True
        else:
            return False

# class IsAuthorOrReadOnly(permissions.BasePermission):
#     # Read-only permissions are allowed for any request
#     def has_object_permission(self, request, view, obj):
#         if request.method == "POST":
#             return False
#         else:
#             return True
# class IsCustomerOrReadOnly(BasePermission):
#     """ Check if user is buyer and logged in then grants access."""
#
#     def has_permission(self, request, view):
#         return bool(
#             request.method in SAFE_METHODS or
#             request.user and
#             request.user.is_authenticated and
#             request.user.role == 'BY'
#         )
# class ReadOnly(BasePermission):
#     """Allow ReadOnly permissions if the request is a safe method"""
#
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS

        #return request.method in SAFE_METHODS

    # def has_object_permission(self, request, view, obj):
    #     print("hiiiiiiiiiiii.....")
    #     print(request.method)
    #     # print('user hi:', request.user.id)
    #     user = request.user
    #     if user.role == 'vendor' and user.id == obj.id:
    #         return True
    #     return False
        # if request.method in SAFE_METHODS:
        #     return True
        # if user.role == 'vendor':
        #     return True
        # return False
