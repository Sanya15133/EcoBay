from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('item/', views.list_items, name='list_items'),
    path('skill/', views.list_skills, name='list_skills'),
    path('skills-request/', views.request_skill, name='request_skill'),
    path('add-item/', views.add_item, name='add_item'),
    path('add-skill/', views.add_skill, name='add_skill'),
    path('search/', views.search, name='search'),
    path('item/<int:id>/', views.get_item, name='get_item'),
    path('skill/<int:id>/', views.get_skill, name='get_skill'),
    path('', views.home, name='home'),
]