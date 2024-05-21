from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView

# Create your views here.

class UserAuthMixin(UserPassesTestMixin):
    def test_func(self):
        # Verifica si el usuario está autenticado y es un superusuario.
        return self.request.user.is_authenticated and self.request.user.is_superuser

    def handle_no_permission(self):
        # Devuelve una respuesta HTTP 403 Forbidden si no se cumple la prueba.
        return HttpResponseForbidden("You don't have permission to access this page.")

class ProtectedView(UserAuthMixin, TemplateView):
       template_name = 'core/protected.html'