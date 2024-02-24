from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import NearMissList
from .serializers import NearMissListSerializer


class NearMissListView(APIView):
    def get(self, request, format=None):
        nearMissList = NearMissList.objects.all()[0:4] 
        serializer = NearMissListSerializer(nearMissList, many=True)
        return Response(serializer.data)