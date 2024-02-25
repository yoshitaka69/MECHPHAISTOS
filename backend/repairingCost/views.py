from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Pm02,Pm03,Pm04,Pm05
from .serializers import Pm02Serializer,Pm03Serializer,Pm04Serializer,Pm05Serializer


class Pm02ViewSet(viewsets.ModelViewSet):
    queryset = Pm02.objects.all()
    serializer_class = Pm02Serializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        pm02 = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(pm02)
        return Response(serializer.data)

    
class Pm03ViewSet(viewsets.ModelViewSet):
    queryset = Pm03.objects.all()
    serializer_class = Pm03Serializer

    def list(self, request:Request):
        pm03 = Pm03.objects.all()
        serializer = Pm03Serializer(pm03, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Pm03.objects.all()
        pm03 = get_object_or_404(queryset, pk=pk)
        serializer = Pm03Serializer(pm03)
        return Response(serializer.data)
    
class Pm04ViewSet(viewsets.ModelViewSet):
    queryset = Pm04.objects.all()
    serializer_class = Pm04Serializer

    def list(self, request:Request):
        pm04 = Pm04.objects.all()
        serializer = Pm04Serializer(pm04, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Pm04.objects.all()
        pm04 = get_object_or_404(queryset, pk=pk)
        serializer = Pm04Serializer(pm04)
        return Response(serializer.data)

class Pm05ViewSet(viewsets.ModelViewSet):
    queryset = Pm05.objects.all()
    serializer_class = Pm05Serializer

    def list(self, request:Request):
        pm05 = Pm05.objects.all()
        serializer = Pm05Serializer(pm05, many=True)
        return Response(serializer.data)

def retrieve(self, request, pk=None):
        queryset = Pm05.objects.all()
        pm05 = get_object_or_404(queryset, pk=pk)
        serializer = Pm05Serializer(pm05)
        return Response(serializer.data)
