from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import FileManagerSerializer
from .models import FileManager


class FileManagerView(APIView):
    def get(self, request):
        files = FileManager.objects.all()
        serializer = FileManagerSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
