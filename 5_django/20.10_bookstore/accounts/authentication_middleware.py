# authentication_middleware.py
from django.shortcuts import redirect

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = None
        if not request.user.is_authenticated:
            # Si el usuario no está autenticado, redirigirlo a la página de inicio 
            response = redirect('book_list')  #

        if response:
            return response

        response = self.get_response(request)

        return response