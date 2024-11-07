from django.urls import path

from app_blogs import views

app_name = 'blogs'

urlpatterns = [
    path('users/', views.user_list_view, name='user_list'),
    path('users/<int:pk>/', views.user_detail_view, name='users_detail'),
    path('blogs/', views.blog_list_create, name='blog_list'),
    path('blogs/<int:pk>/', views.blog_detail_update_delete, name='blog_detail'),
    path('blogs/users/<int:pk>/', views.blog_detail_update_delete, name='api_user_list'),
]
