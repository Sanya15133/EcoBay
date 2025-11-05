from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/register', views.register, name='register'),
    path('/login', views.login, name='login'),
    path('/items', views.login, name='login'),
    path('/skills', views.login, name='login'),
]