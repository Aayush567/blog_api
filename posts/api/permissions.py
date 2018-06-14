from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    object-level permission to only allow owners of an object to edit it.

    """
    message = 'You must be owner of this object.'
    my_safe_method = ['PUT']
    def has_object_permission(self, request, view, obj):
        my_safe_method = ['PUT']
        if request.method in my_safe_method:
            return True

        return obj.user == request.user



    def has_permission(self, request, view):
        if request.method in self.my_safe_method:
            return True
        return False




