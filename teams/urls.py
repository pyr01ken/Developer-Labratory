from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    path('', views.TeamView.as_view(), name='teams'),
    path('task/', views.TaskView.as_view(), name='tasks'),
]
