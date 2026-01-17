from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('skills-request/', views.request_skill, name='request_skill'),
    path('add-item/', views.item_categories, name='item_categories'),
    path('add-item/', views.add_item, name='add_item'),
    path('add-skill/', views.add_skill, name='add_skill'),
    path('search/', views.search, name='search'),
    path('item/<int:id>/make_offer', views.make_offer, name='make_offer'),
    path('item/<int:id>/', views.get_item, name='get_item'),
    path('skill/<int:id>/', views.get_skill, name='get_skill'),
    path('', views.home, name='home'),
]