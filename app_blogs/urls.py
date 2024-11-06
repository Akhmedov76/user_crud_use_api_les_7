from django.urls import path

from app_blogs import views

app_name = 'blogs'

urlpatterns = [
    path('users/', views.user_list_view, name='user_list'),
    path('users/<int:pk>/', views.user_detail_view, name='users_detail')

]
