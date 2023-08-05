from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.UsersListView.as_view(), name='users'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('activate-account/<str:email_active_code>/', views.ActivateAccountView, name='activate_account'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
