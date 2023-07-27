from django.urls import path
from . import views

app_name = 'files'

urlpatterns = [
    path('', views.FileManagerView.as_view(), name='files')
]