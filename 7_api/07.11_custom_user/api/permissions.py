from rest_framework.permissions import BasePermission, SAFE_METHODS

class ReadOnlyOrAuthenticatedWritePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
    
#aalo lecture to everybody but writing just to authenticated
