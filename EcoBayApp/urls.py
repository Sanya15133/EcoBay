from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/register', views.register, name='register'),
    path('/login', views.login, name='login'),
    path('/items', views.list_items, name='list_items'),
    path('/skills', views.list_skills, name='list_skills'),
]