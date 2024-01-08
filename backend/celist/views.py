from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CeList
from .serializers import CeListSerializer


class LatestCeList(APIView):
    def get(self, request, format=None):
        celist = CeList.objects.all()[0:4] 
        serializer = CeListSerializer(celist, many=True)
        return Response(serializer.data)