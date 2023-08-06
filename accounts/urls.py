from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.UsersListView.as_view(), name='users'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('activate-account/<str:email_active_code>/', views.ActivateAccountView.as_view(), name='activate_account'),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset-password/<str:active_code>/', views.ResetPasswordView.as_view(), name='reset_password'),
]

