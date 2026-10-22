from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('skills-request/', views.request_skill, name='request_skill'),
    path('add-item/', views.add_item, name='add_item'),
    path('add-event/', views.add_event, name='add_event'),
    path('add-notice/', views.add_notice, name='add_notice'),
    path('add-skill/', views.add_skill, name='add_skill'),
    path('search/', views.search, name='search'),
    path('item/make_offer/<int:id>', views.make_offer, name='make_offer'),
    path('item/delete/<int:id>', views.delete_item, name='delete_item'),
    path('notice/delete/<int:id>', views.delete_notice, name='delete_notice'),
    path('skill/delete/<int:id>', views.delete_skill, name='delete_skill'),
    path('event/delete/<int:id>', views.delete_event, name='delete_event'),
    path('item/<int:id>/', views.get_item, name='get_item'),
    path('notice/<int:id>/', views.get_notice, name='get_notice'),
    path('event/<int:id>/', views.get_event, name='get_event'),
    path('skill/<int:id>/', views.get_skill, name='get_skill'),
    path('', views.home, name='home'),
]