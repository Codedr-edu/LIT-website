from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('story/', views.story, name='story'),
    path('news/', views.news, name='news'),
    path('event/', views.event, name='event'),
    path('members/', views.members, name='members'),
    path('contact/', views.contact, name='contact'),
    path('create/news/', views.create_news, name='create_news'),
    path('create/event/', views.create_event, name='create_event'),
    path('create/members/', views.create_members, name='create_members'),
    path('news/<int:id>/', views.news_view, name='news_view'),
    path('event/<int:id>/', views.event_view, name='event_view'),
    path('members/<int:id>/', views.members_view, name='members_view'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
