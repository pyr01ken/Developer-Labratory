from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.TestProjectView.as_view(), name='test')
]