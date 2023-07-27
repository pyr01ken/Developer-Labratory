from rest_framework import serializers
from .models import FileManager


class FileManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileManager
        fields = '__all__'
