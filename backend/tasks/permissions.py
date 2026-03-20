from rest_framework import permissions

class IsAdminOrOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a task or admin to edit/delete it.
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to anyone (but filtered in view)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Admin can do anything
        if request.user.role == 'admin':
            return True
        
        # Otherwise, only the owner can edit/delete
        return obj.created_by == request.user