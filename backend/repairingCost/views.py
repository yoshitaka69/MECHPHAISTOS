from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import RepairingCostPM02
from .serializers import RepairingCostPM02Serializer


class RepairingCostPM02View(APIView):
    def get(self, request, format=None):
        repairingCostPM02 = RepairingCostPM02.objects.all()[0:4] 
        serializer = RepairingCostPM02Serializer(repairingCostPM02, many=True)
        return Response(serializer.data)
