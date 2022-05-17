from django.urls import path
from .views import home_view, register, password_change
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_view, name="home"),
    path('register', register, name='register'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="registration/password_change.html"), name="password_change")
]