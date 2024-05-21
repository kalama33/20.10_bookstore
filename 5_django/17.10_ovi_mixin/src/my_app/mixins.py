from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class AuthenticatedUserMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('admin:index')
        return super().dispatch(request, *args, **kwargs)