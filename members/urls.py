from django.urls import path
from . import views
from django.contrib.auth import views as authViews


urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    
    path('reset_password/', authViews.PasswordResetView.as_view(
        template_name='authenticate/reset_password.html'), name='reset_password'),
    
    path('password_reset/done/', authViews.PasswordResetDoneView.as_view(
        template_name='authenticate/reset_password_done.html'), name='reset_password_done'),
    
    path('reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(
        template_name='authenticate/reset_password_confirm.html'), name='reset_password_confirm'),
    
    path('reset/done/', authViews.PasswordResetCompleteView.as_view(
        template_name='authenticate/reset_password_complete.html'), name='reset_password_complete'),
]