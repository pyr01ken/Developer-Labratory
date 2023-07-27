from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer


class UsersListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
