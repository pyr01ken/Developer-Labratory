from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Team, Task
from .serializer import TeamSerializer, TaskSerializer


class TeamView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
