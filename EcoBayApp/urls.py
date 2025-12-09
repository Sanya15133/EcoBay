from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('items', views.list_items, name='list_items'),
    path('skills', views.list_skills, name='list_skills'),
    path('skills-request', views.request_skill, name='request_skill'),
    path('add-items', views.add_item, name='add_item'),
    path('add-skill', views.add_skill, name='add_skill'),
]