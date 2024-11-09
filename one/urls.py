from django.urls import path
from django.contrib.auth import views as auth_views
from .views import contact_view
from .views import contact_view, register_view

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
