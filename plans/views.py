from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import PlanSerializer
from .models import Plan


class PlanView(APIView):
    def get(self, request):
        plans = Plan.objects.all()
        serializer = PlanSerializer(plans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
