from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('delete_post/<pk>/', views.delete_post, name='delete_post'),
    path('create_post/', views.create_post, name='create_post'),
    path('delete_comment/<pk>/', views.delete_comment, name='delete_comment'),
    path('create_comment/<pk>/', views.create_comment, name='create_comment'),
    path('my_posts/', views.my_posts, name='my_posts'),
]
