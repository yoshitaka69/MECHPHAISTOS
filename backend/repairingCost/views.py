from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Pm02,Pm03,Pm04,Pm05
from .serializers import Pm02Serializer,Pm03Serializer,Pm04Serializer,Pm05Serializer


class Pm02View(APIView):
    def get(self, request, format=None):
        pm02 = Pm02.objects.all()[0:4] 
        serializer = Pm02Serializer(pm02, many=True)
        return Response(serializer.data)
    
class Pm03View(APIView):
    def get(self, request, format=None):
        pm03 = Pm03.objects.all()[0:4] 
        serializer = Pm03Serializer(pm03, many=True)
        return Response(serializer.data)
    
class Pm04View(APIView):
    def get(self, request, format=None):
        pm04 = Pm04.objects.all()[0:4] 
        serializer = Pm04Serializer(pm04, many=True)
        return Response(serializer.data)
    
class Pm05View(APIView):
    def get(self, request, format=None):
        pm05 = Pm05.objects.all()[0:4] 
        serializer = Pm05Serializer(pm05, many=True)
        return Response(serializer.data)
