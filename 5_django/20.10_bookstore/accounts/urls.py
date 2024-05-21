from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # URL for user registration (e.g., /accounts/signup/)
    path('signup/', views.signup, name='signup'),

    # URL for user login (e.g., /accounts/login/)
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # URL for user logout (e.g., /accounts/logout/)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
