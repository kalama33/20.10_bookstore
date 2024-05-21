from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class AuthenticatedUserMixin(AccessMixin):
#"""Ensure user is authenticated before accessing the view."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect to your login URL
        return super().dispatch(request, *args, **kwargs)

#Create a mixin that checks if the user is staff:

class AuthenticatedStaffMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('login') 
        return super().dispatch(request, *args, **kwargs)